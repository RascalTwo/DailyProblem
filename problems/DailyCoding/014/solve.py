import random



def solve(n: int = 100000000) -> float:
	return (8 * sum(random.random()**2 + random.random()**2 <= 0.5 for _ in range(n))) / n


def test_solve():
	assert str(solve())[:5] == '3.141'
