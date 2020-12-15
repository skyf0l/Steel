from datetime import datetime
from hashlib import sha256

class Transaction:

	def __init__(self, input, output, amount):
		self.timestamp = datetime.now()

		self.input = input
		self.output = output
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