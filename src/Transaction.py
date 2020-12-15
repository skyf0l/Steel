from datetime import datetime
from hashlib import sha256

from .Wallet import Wallet

class Transaction:

	def __init__(self, input, output, amount):
		self.timestamp = datetime.now()

		if input == None:
			self.input = 'REWARD'
		else:
			self.input = input.address
		self.output = output.address
		self.amount = amount

		self.hash = self.generate_hash()

	def verify(self):
		if self.amount < 0:
			return False
		return True

	def generate_hash(self):
		transaction_data = str(self.timestamp) + str(self.input) + str(self.output) + str(self.amount)
		transaction_hash = sha256(transaction_data.encode())
		return transaction_hash.hexdigest()

	def print(self, tab_count=0):
		tabs = '\t' * tab_count
		print(tabs + 'Hash: {}'.format(self.hash))
		print(tabs + 'Timestamp: {}'.format(self.timestamp))
		print(tabs + 'Input: {}'.format(self.input))
		print(tabs + 'Output: {}'.format(self.output))
		print(tabs + 'Amount: {}'.format(self.amount))