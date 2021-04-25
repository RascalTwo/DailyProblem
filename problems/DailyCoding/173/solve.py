from typing import Any, Dict



def solve(nested_dict: Dict[str, Any], prefix: str = '') -> Dict[str, Any]:
	new_dict: Dict[str, Any] = {}
	for key, value in nested_dict.items():
		prefixed_key = f'{prefix}{key}'
		if isinstance(value, dict):
			new_dict.update(solve(value, prefixed_key + '.'))  # type: ignore
		elif isinstance(value, list):
			new_dict.update(solve(dict(enumerate(value)), prefixed_key + '.'))
		else:
			new_dict[prefixed_key] = value

	return new_dict


def test_solve():
	assert solve({
		'key': 3,
		'foo': {
			'a': 5,
			'bar': {
				'baz': 8
			}
		}
	}) == {
		'key': 3,
		'foo.a': 5,
		'foo.bar.baz': 8
	}
	assert solve({
		'key': 3,
		'arr': ['a', 'b', 'c']
	}) == {
		'key': 3,
		'arr.0': 'a',
		'arr.1': 'b',
		'arr.2': 'c'
	}
