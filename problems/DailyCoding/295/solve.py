from typing import Dict, List



def solve(height: int) -> str:
	if not height:
		return ''

	rows: List[Dict[int, int]] = [{0: 1}]
	for _ in range(height):
		last = rows[-1]
		indexes = list(last.keys())
		start = min(indexes)
		end = max(indexes)
		row = {
			start - 1: last[start],
			end + 1: last[end]
		}
		for i in range(start + 1, end + 1, 2):
			row[i] = last[i - 1] + last[i + 1]
		rows.append(row)

	return '\n'.join([
		(' ' * i) + ' '.join(
			str(value)
			for _, value in sorted(
				row.items(),
				key = lambda pair: pair[0]
			)
		)
		for i, row in enumerate(rows[::-1])
	][::-1])


def test_solve():
	assert '\n' + solve(4) + '\n' == '''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
