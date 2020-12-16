import random
import statistics



def rand7():
	return random.randint(1, 7)


def rand5() -> int:
	while True:
		if num := rand7() <= 5:
			return num


def test_solve():
	assert 3.8 <= statistics.mean([rand7() for _ in range(1000000)]) <= 4.2
	assert 2.8 <= statistics.mean([rand5() for _ in range(1000000)]) <= 3.2
