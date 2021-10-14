from typing import Dict, List, Optional, Tuple



def solve(mice: List[int], holes: List[int]) -> Dict[int, int]:
	closest_mice = {
		hole: {
			mouse: abs(hole - mouse)
			for mouse in mice
		}
		for hole in holes
	}

	mice_hole_mappings: Dict[int, int] = {}
	for _ in range(len(mice)):
		best: Optional[Tuple[int, int, int]] = None
		for hole, distances in closest_mice.items():
			smallest = min(distances.items(), key = lambda pair: pair[1])
			if best is None or smallest[1] > best[2]:
				best = (hole, *smallest)
		assert best
		hole, mouse, _ = best

		for distances in closest_mice.values():
			del distances[mouse]
		del closest_mice[hole]
		mice_hole_mappings[mouse] = hole

	return mice_hole_mappings


def test_solve():
	assert solve([1, 4, 9, 15], [10, -5, 0, 16]) == {
    1: -5,
    4: 0,
    9: 10,
    15: 16
	}
test_solve()