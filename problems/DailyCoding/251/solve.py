import random
import string
import heapq
import os

from typing import Iterator, List, Tuple



def load_values(filepath: str) -> Iterator[int]:
	with open(filepath, 'rb') as file:
		while True:
			int_bytes = file.read(32)
			if not int_bytes:
				break
			yield int.from_bytes(int_bytes, byteorder='big')


def save_values(filepath: str, values: List[int]):
	with open(filepath, 'wb') as file:
		for value in values:
			file.write(value.to_bytes(32, byteorder='big'))


def solve(input_filepaths: List[str], output_template: string.Template, memory_limit: int):
	for filepath in input_filepaths:
		save_values(filepath, sorted(load_values(filepath)))


	queue: List[Tuple[int, int, Iterator[int]]] = []
	for filepath in input_filepaths:
		iterator = load_values(filepath)
		value = next(iterator)
		heapq.heappush(queue, (value, len(queue), iterator))


	i = 0
	values: List[int] = []
	while queue:
		value, pq_dummy, iterator = heapq.heappop(queue)
		values.append(value)
		if len(values) >= memory_limit:
			save_values(output_template.substitute(i=i), values)
			i += 1
			values = []
		try:
			heapq.heappush(queue, (next(iterator), pq_dummy, iterator))
		except StopIteration:
			pass
	if values:
		save_values(output_template.substitute(i=i), values)


def cleanup_files(dir_path: str):
	for filename in os.listdir(dir_path):
		if filename.endswith('.bin'):
			os.unlink(os.path.join(dir_path, filename))


def test_solve():
	def assert_solve(values: List[int], memory_limit: int):
		dir_path = os.path.dirname(os.path.realpath(__file__))
		cleanup_files(dir_path)

		filepaths: List[str] = []

		for i in range((len(values) + memory_limit - 1) // memory_limit):
			filepath = os.path.join(dir_path, f'values.{i}.bin')
			filepaths.append(filepath)
			save_values(filepath, values[i * memory_limit:(i + 1) * memory_limit])

		output_template = string.Template(os.path.join(dir_path, 'output.${i}.bin'))
		solve(filepaths, output_template, memory_limit)
		sorted_values = sorted(values)

		read_values: List[int] = []
		for i in range(len(filepaths)):
			read_values.extend(load_values(output_template.substitute(i=i)))
		cleanup_files(dir_path)

		assert read_values == sorted_values

	assert_solve([random.randint(0, 100) for _ in range(105)], 10)
	assert_solve([random.randint(0, 1000000000) for _ in range(1000000)], 1000)
