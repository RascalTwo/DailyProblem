from typing import Dict, Iterable, List



def solve(*user_preferences: List[int]) -> Iterable[int]:
	songs: Dict[int, List[int]] = {}
	for preferences in user_preferences:
		for s, song in enumerate(preferences):
			if song not in songs:
				songs[song] = []
			songs[song].append(s)

	while songs:
		song = min(
			(user_preferences[i][0] for i in range(len(user_preferences)) if len(user_preferences[i])),
			key = lambda song: len(songs[song])
		)
		yield song
		del songs[song]
		for preferences in user_preferences:
			if song in preferences:
				preferences.remove(song)


def test_solve():
	assert list(solve([1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5])) == [2, 1, 6, 7, 3, 9, 5]
