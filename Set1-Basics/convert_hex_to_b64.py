import binascii
import base64

def convert_hex_to_b64(s):
	data = binascii.unhexlify(s)
	return base64.b64encode(data)

enc = convert_hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696"
				         "b65206120706f69736f6e6f7573206d757368726f6f6d")
if enc == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
	print("Success")
print(enc)