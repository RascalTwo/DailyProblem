import random
import statistics


from typing import List, Optional



def solve(*values: int):
	count = 0
	rolls: List[Optional[int]] = [None] * len(values)
	while tuple(rolls) != values:
		rolls.pop(0)
		rolls.append(random.randint(1, 6))
		count += 1

	return count


def test_solve():
	for required in [(5, 6), (5, 5)]:
		rolls: List[int] = [solve(*required) for _ in range(100)]
		print(f'Req  : {required}\nTotal: {sum(rolls)}\nAvg  : {sum(rolls) / len(rolls)}\nDev  : {statistics.stdev(rolls)}\nVar  : {statistics.variance(rolls)}')
