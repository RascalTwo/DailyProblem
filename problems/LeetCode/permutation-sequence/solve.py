import itertools



def solve(n: int, k: int) -> str:
	return sorted(''.join(perm) for perm in itertools.permutations(list(map(str, range(1, n + 1)))))[k - 1]


def test_solve():
	assert solve(3, 3) == '213'
	assert solve(4, 9) == '2314'
	assert solve(3, 1) == '123'
