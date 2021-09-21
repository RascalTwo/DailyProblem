from typing import Tuple



def solve(time: str) -> Tuple[float, float, float]:
	hour, minute = map(int, time.split(':'))

	minute_degree = 360 / 60 * minute
	hour_degree = 360 / 12 * hour + (360 / 12 * (minute / 60))

	return hour_degree % 360, minute_degree % 360, abs(hour_degree - minute_degree) % 360


def test_solve():
	assert solve('12:00') == (0, 0, 0)
	assert solve('6:00') == (180, 0, 180)
	assert solve('6:30') == (195, 180, 15)
	assert solve('9:45') == (292.5, 270, 22.5)
