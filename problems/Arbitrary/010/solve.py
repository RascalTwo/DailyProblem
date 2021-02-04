from typing import List



def merge(*strings: str) -> str:
	result = ''

	for i in range(len(strings[0])):
		for string in strings:
			result += string[i]

	return result


def split(string: str, k: int) -> List[str]:
	if len(string) % k != 0:
		raise ValueError(f'"{string}" can not be evenly broken into {k} words')

	words = [''] * k

	for i, char in enumerate(string):
		words[i % k] += char

	return words


def test_solve():
	assert merge('ABC', '123') == 'A1B2C3'
	assert merge('hello', 'world') == 'hweolrllod'
	assert merge('---', '===', '___') == '-=_-=_-=_'


	for string, length in (('1234567', 6), ('12345', 6)):
		try:
			split(string, length)
			assert False, 'exception missing'
		except ValueError:
			pass

	assert split('A1B2C3', 2) == ['ABC', '123']
	assert split('hweolrllod', 2) == ['hello', 'world']
	assert split('-=_-=_-=_', 3) == ['---', '===', '___']
