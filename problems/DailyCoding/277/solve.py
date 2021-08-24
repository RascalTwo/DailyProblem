from typing import Optional



def solve(*integers: int) -> Optional[str]:
	count = len(integers)
	if count == 1:
		count = 0
	first = bin(integers[0])[2:].rjust(8, '0')
	if not first.startswith(('1' * count) + '0'):
		return

	for integer in integers[1:]:
		if not bin(integer)[2:].rjust(8, '0').startswith('10'):
			return

	return bytearray(integers).decode()


def test_solve():
	assert solve(0b11100010, 0b10000010, 0b10101100) == '€'
	assert solve(0b01100010, 0b00000010, 0b10101100) is None
	assert solve(0b11110000, 0b10011111, 0b10010110, 0b10010110) == '🖖'
	assert solve(0b01110000, 0b10101010) is None
	assert solve(0b01100001) == 'a'
	assert solve(0b11100001) is None
	assert solve(0b11110000, 0b10011111, 0b10010010, 0b10101001) == '💩'
	assert solve(0b11100000, 0b10011111, 0b10010010, 0b10101001) is None
	assert solve(0b11000010, 0b10101110) == '®'

