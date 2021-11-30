from typing import List, Literal, Tuple, Union


Action = Union[Literal['pickup'], Literal['dropoff']]
Event = Tuple[int, int, Action]

def solve(*events: Event):
	total = 0
	packages = {}
	waiting: List[Event] = list(events)
	waiting.reverse()
	while waiting:
		id, timestamp, action = waiting.pop()
		if action == 'pickup':
			packages[id] = timestamp
			continue
		if id not in packages:
			waiting.insert(0, (id, timestamp, action))
			continue
		total += timestamp - packages[id] 
		continue

	return total



def test_solve():
	assert solve(
		(1, 1570320047, 'pickup' ),
    (1, 1570320725, 'dropoff'),
    (2, 1570321092, 'pickup' ),
    (3, 1570321212, 'pickup' ),
    (3, 1570322352, 'dropoff'),
    (2, 1570323012, 'dropoff'),
	) == 3738
