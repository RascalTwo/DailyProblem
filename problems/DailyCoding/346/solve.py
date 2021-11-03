import sys

from typing import Dict, List, Tuple

Flight = Tuple[str, str, int]



def travel(flight_map: Dict[str, Dict[str, int]], source: str, dest: str, connections: int) -> Tuple[List[str], int]:
    if source == dest:
        return [dest], 0

    if not connections:
        return [], 0

    best: Tuple[List[str], int] = ([], sys.maxsize)
    for hop_dest, cost in flight_map.get(source, {}).items():
        path, path_cost = travel(flight_map, hop_dest, dest, connections - 1)
        total_cost = path_cost + cost
        if path and total_cost < best[1]:
            best = ([source] + path, total_cost)

    return best


def solve(flights: List[Flight], source: str, dest: str, connections: int) -> List[str]:
    flight_map: Dict[str, Dict[str, int]] = {}
    for source, dest, cost in flights:
        flight_map.setdefault(source, {})[dest] = cost

    return travel(flight_map, source, dest, connections)[0]


def test_solve():
	assert solve([
        ('JFK', 'ATL', 150),
        ('ATL', 'SFO', 400),
        ('ORD', 'LAX', 200),
        ('LAX', 'DFW', 80),
        ('JFK', 'HKG', 800),
        ('ATL', 'ORD', 90),
        ('JFK', 'LAX', 500),
	], 'JFK', 'LAX', 3) == ['JFK', 'ATL', 'ORD', 'LAX']
	assert solve([
        ('JFK', 'ATL', 1500),
        ('ATL', 'SFO', 400),
        ('ORD', 'LAX', 200),
        ('LAX', 'DFW', 80),
        ('JFK', 'HKG', 800),
        ('ATL', 'ORD', 90),
        ('JFK', 'LAX', 500),
	], 'JFK', 'LAX', 3) == ['JFK', 'LAX']