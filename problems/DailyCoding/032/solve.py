from typing import Dict, List, Optional


def solve(exchange_rates: Dict[str, Dict[str, float]], path: Optional[List[str]] = None, value: float = 1) -> Optional[List[str]]:
	if not path:
		path = ['A']

	is_not_start = len(path) > 1
	current = path[-1]
	if current == path[0] and is_not_start:
		return path if value > 1 else None


	for dest, change in exchange_rates[current].items():
		if is_not_start and dest == path[-2]:
			continue

		if (found := solve(exchange_rates, [*path, dest], value * change)):
			return found


def test_solve():
	assert solve({
		'A': {'B': 1},
		'B': {'A': 1, 'C': 0.95},
		'C': {'A': 1.1, 'B': 1.05}
	}) == ['A', 'B', 'C', 'A']

	assert solve({
		'A': {'B': 1},
		'B': {'A': 1, 'C': 0.1},
		'C': {'A': 1.1, 'B': 1.1}
	}) is None
