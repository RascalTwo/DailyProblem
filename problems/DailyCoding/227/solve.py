from typing import List, Tuple



Location = Tuple[int, int]


def attempt(matrix: List[List[str]], dictionary: List[str], current: Location, visited: List[Location], collected: List[str], word: str) -> List[str]:
	if current in visited or not any(dword.startswith(word) for dword in dictionary):
		return collected
	visited.append(current)

	possible_neighbors: List[Tuple[Location, str]] = []
	for offsets in ((0, 1), (1, 0), (0, -1), (-1, 0)):
		nr, nc = [cord + offsets[i] for i, cord in enumerate(current)]
		if nr < 0 or nr >= len(matrix):
			continue
		if nc < 0 or nc >= len(matrix[nr]):
			continue
		nloc = (nr, nc)
		if nloc in visited:
			continue
		possible_neighbors.append((nloc, matrix[nr][nc]))


	most = collected

	for _ in range(2):
		for nloc, char in possible_neighbors:
			most = max(most, attempt(matrix, dictionary[:], nloc, visited[:], collected[:], word + char), key=len)

		if word not in dictionary:
			break

		dictionary.remove(word)
		collected.append(word)
		word = ''

	return most


def solve(matrix: List[List[str]], dictionary: List[str]) -> List[str]:
	most: List[str] = []

	for r, row in enumerate(matrix):
		for c, col in enumerate(row):
			most = max(most, attempt(matrix, dictionary[:], (r, c), [], [], col), key=len)

	return list(most)


def test_solve():
	assert solve([
		['1', '2', '3', '4'],
		['6', '5', '4', '5'],
		['7', '2', '3', '6'],
		['8', '9', '8', '7']
	], ['12', '34', '56', '78', '98', '76', '54', '32']) == ['12', '34', '56', '78', '98', '76', '54', '32']
	assert solve([
		['1', '2', '3', '4'],
		['2', '3', '4', '5'],
		['3', '4', '5', '6'],
		['4', '5', '6', '7']
	], ['1234', '567', '654', '3432']) == ['1234', '567', '654', '3432']
	assert solve([
		['1', '2', '3', '4'],
		['2', '3', '4', '5'],
		['3', '4', '5', '6'],
		['4', '5', '6', '7']
	], ['1234', '567', '654', '3432', '12', '34']) == ['12', '34', '567', '654', '3432']
