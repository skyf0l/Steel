import ecdsa
from hashlib import sha256

class Wallet:

	def __init__(self, name):
		self.address = name

		sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1, hashfunc=sha256)

		self.privatekey = sk
		self.publickey = sk.get_verifying_key()

		'''
		print(sk.to_string().hex())
		vk = sk.get_verifying_key()
		print(vk.to_string().hex())
		sig = sk.sign(b"message")
		print(sig.hex())
		print(vk.verify(sig, b"message"))
		exit()'''