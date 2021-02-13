import random



def solve(n: int):
	def get_head_count(count: int):
		return sum(coin == 'head' for coin in (random.choice(['head', 'tail']) for _ in range(count)))

	reflips = 0

	heads = get_head_count(n)
	while heads > 1:
		heads = get_head_count(heads)

		reflips += 1

	return reflips


def test_solve():
	for n in [10, 100, 1000, 10000, 100000, 1000000]:
		print(n, solve(n))
