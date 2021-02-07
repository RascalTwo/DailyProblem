def xor_cipher(plaintext: str, key: str) -> str:
	return ''.join(chr(ord(plaintext[i]) ^ ord(key[i % len(key)])) for i in range(len(plaintext)))


def test_solve():
	for plaintext, key in (('Hello, World!', 'mouse'), ('abc123', 'universal')):
		encoded = xor_cipher(plaintext, key)
		assert xor_cipher(encoded, key) == plaintext
