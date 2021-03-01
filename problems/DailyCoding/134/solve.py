import collections


from typing import DefaultDict, List



class SparseArray:
	def __init__(self, arr: List[int]=[], size: int=0):
		self.values: DefaultDict[int, int] = collections.defaultdict(int)
		for i, val in enumerate(arr):
			if val:
				self.values[i] = val


	def set(self, i: int, val: int):
		if val:
			self.values[i] = val


	def get(self, i: int) -> int:
		return self.values.get(i, 0)


	def __len__(self):
		return len(self.values)



def test_solve():
	sa = SparseArray([0, 0, 1, 0, 0, 2, 0])

	assert len(sa) == 2
	assert sa.get(2) == 1
	assert sa.get(5) == 2

	sa.set(10, 9)
	assert len(sa) == 3
	assert sa.get(10) == 9
