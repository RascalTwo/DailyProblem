from typing import Iterable, List, Optional, Tuple



def compute_itinerary(flights: List[Tuple[str, str]], origin: str) -> Iterable[List[str]]:
	next_flights = [flight for flight in flights if flight[0] == origin]
	if next_flights == flights:
		yield from [[flights[0][1]]]
		return

	for next_flight in next_flights:
		yield from [
			[next_flight[1], *branch]
			for branch in compute_itinerary([flight for flight in flights if flight != next_flight], next_flight[1])
		]


def solve(flights: List[Tuple[str, str]], origin: str) -> Optional[List[str]]:
	raw_paths = list(compute_itinerary(flights, origin))
	if not raw_paths:
		return None

	return [origin] + sorted('-'.join(path) for path in raw_paths)[0].split('-')


def test_solve():
	assert solve([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
	assert solve([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None
	assert solve([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') == ['A', 'B', 'C', 'A', 'C']
