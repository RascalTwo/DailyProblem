import random
import statistics



def rand5():
	return random.randint(1, 5)


def rand7():
	while True:
		if num := 5 * rand5() + rand5() - 5 < 21:
			return (num % 7) + 1


def test_solve():
	assert 3.8 <= statistics.mean([rand7() for _ in range(1000000)]) <= 4.2
	assert 2.8 <= statistics.mean([rand5() for _ in range(1000000)]) <= 3.2