from typing import List, Tuple

Point = Tuple[int, int]



def solve_brute(matrix: List[List[int]], smaller: Point, larger: Point) -> Tuple[int, int]:
	small_value = matrix[smaller[0]][smaller[1]]
	large_value = matrix[larger[0]][larger[1]]

	counts = 0 + 0j

	for row in matrix:
		for cell in row:
			if cell < small_value:
				counts += 1
			elif cell > large_value:
				counts += 1j

	return int(counts.real), int(counts.imag)


def solve_smart(matrix: List[List[int]], smaller: Point, larger: Point) -> Tuple[int, int]:
	small_value = matrix[smaller[0]][smaller[1]]
	large_value = matrix[larger[0]][larger[1]]

	counts = 0 + 0j

	for row in matrix:
		for cell in row:
			if cell >= small_value:
				break
			counts += 1

	for row in matrix:
		for cell in row[::-1]:
			if cell <= large_value:
				break
			counts += 1j

	return int(counts.real), int(counts.imag)


def test_solve():
	for solve in (solve_brute, solve_smart):
		assert solve([
			[1 , 3 , 4 , 10, 15, 20],
			[2 , 6 , 9 , 14, 22, 25],
			[3 , 8 , 10, 15, 25, 30],
			[10, 11, 12, 23, 30, 35],
			[20, 25, 30, 35, 40, 45]
		], (1, 1), (3, 3)) == (5, 10)
