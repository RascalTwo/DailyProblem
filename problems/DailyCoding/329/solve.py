from typing import Dict, List



def solve(guy_preferences: Dict[str, List[str]], gal_preferences: Dict[str, List[str]]):
	pairings: Dict[str, str] = {}
	while guy_preferences:
		best_pairing = None
		for guy, preferences in guy_preferences.items():
			for preference in preferences:
				score = -preferences.index(preference) + -gal_preferences[preference].index(guy)
				if best_pairing is None or score > best_pairing[2]:
					best_pairing = (guy, preference, score)

		assert best_pairing
		guy, girl, _ = best_pairing
		pairings[guy] = girl

		del gal_preferences[girl]
		for preferences in gal_preferences.values():
			preferences.remove(guy)

		del guy_preferences[guy]
		for preferences in guy_preferences.values():
			preferences.remove(girl)

	return pairings


def test_solve():
	assert solve({
		'andrew': ['caroline', 'abigail', 'betty'],
		'bill': ['caroline', 'betty', 'abigail'],
		'chester': ['betty', 'caroline', 'abigail'],
	}, {
		'abigail': ['andrew', 'bill', 'chester'],
		'betty': ['bill', 'andrew', 'chester'],
		'caroline': ['bill', 'chester', 'andrew']
	}) == {
		'bill': 'caroline',
		'andrew': 'abigail',
		'chester': 'betty'
	}
