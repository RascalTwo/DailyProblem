from typing import List



def solve(array: List[int], k: int, smallest: bool) -> int:
	array = array[:]
	array.sort(reverse=not smallest)
	return array[k]


def test_solve():
	for arr in ([4, 2, 8, 3, 5], ):
		smalls = sorted(arr)
		for i in range(len(smalls)):
			print(solve(arr, i, True), smalls[i])
			assert solve(arr, i, True) == smalls[i]
		bigs = sorted(arr, reverse=True)
		for i in range(len(bigs)):
			print(solve(arr, i, False), bigs[i])
			assert solve(arr, i, False) == bigs[i]
