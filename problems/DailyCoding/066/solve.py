import random
import statistics



def toss_biased():
	return random.choice([0, 1, 1, 1])


def solve():
	tosses = [toss_biased(), toss_biased()]
	while tosses[0] == tosses[1]:
		tosses = [toss_biased(), toss_biased()]
	return tosses[0]


def test_solve():
	assert round(statistics.mean(random.randint(0, 1) for _ in range(1000000)), 1) == 0.5
	assert round(statistics.mean(solve() for _ in range(1000000)), 1) == 0.5
