from typing import Dict



def decode(flags: int, *keys: str) -> Dict[str, bool]:
	results: Dict[str, bool] = {}
	for i in range(max(flags.bit_length(), len(keys))):
		results[keys[i]] = bool(flags >> i & 1)
	return results


def encode(map: Dict[str, bool]) -> int:
	flags = 0
	for i, value in enumerate(map.values()):
		flags |= int(value) << i
	return flags


def test_solve():
	for flags, keys, expected_map in (
		(0b0001, ['User', 'Mod', 'Admin', 'Owner'], {'User': True, 'Mod': False, 'Admin': False, 'Owner': False}),
		(0b101, ['A', 'B', 'C'], {'A': True, 'B': False, 'C': True})
	):
		decoded = decode(flags, *keys)
		assert decoded == expected_map
		assert encode(decoded) == flags
