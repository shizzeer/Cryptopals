import binascii


def fixed_xor(b1, b2):
	return bytes([x ^ y for (x, y) in zip(b1, b2)])


bytes1 = binascii.unhexlify("1c0111001f010100061a024b53535009181c")
bytes2 = binascii.unhexlify("686974207468652062756c6c277320657965")
res = fixed_xor(bytes1, bytes2)
print(res == binascii.unhexlify("746865206b696420646f6e277420706c6179"))