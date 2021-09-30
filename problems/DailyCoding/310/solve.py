import operator



def solve_loop(n: int) -> int:
	set = 0
	for i in range(1, n):
		set += bin(i).count('1')
	return set


def solve_sum(n: int) -> int:
	return sum(map(operator.methodcaller('count', '1'), map(bin, range(1, n))))


def test_solve():
	for solve in (solve_loop, solve_sum):
		assert solve(2) == 1
		assert solve(10) == 15
		assert solve(16) == 32
		assert solve(100) == 316
		assert solve(1000) == 4932
		assert solve(1024) == 5120
		assert solve(1000000) == 9884992
