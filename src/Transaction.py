from datetime import datetime
from hashlib import sha256

from .Wallet import Wallet

class Transaction:

	def __init__(self, inputs, outputs):
		self.timestamp = datetime.now()

		self.inputs = inputs
		self.outputs = outputs

		self.hash = self.generate_hash()

	@staticmethod
	def create_simple_transaction(input, output, amount):
		inputs = {
			'addr': input.address,
			'amount': -amount
		}
		outputs = {
			'addr': output.address,
			'amount': amount
		}
		transaction = Transaction(inputs, outputs)
		return transaction

	@staticmethod
	def create_reward_transaction(output, amount):
		inputs = {
			'REWARD'
		}
		outputs = {
			'addr': output.address,
			'amount': amount
		}
		transaction = Transaction(inputs, outputs)
		return transaction

	def verify(self):
		if self.outputs['amount'] < 0:
				return False
		return True

	def generate_hash(self):
		transaction_data = str(self.timestamp) + str(self.inputs) + str(self.outputs)
		transaction_hash = sha256(transaction_data.encode())
		return transaction_hash.hexdigest()

	def print(self, tab_count=0):
		tabs = '\t' * tab_count
		print(tabs + 'Hash: {}'.format(self.hash))
		print(tabs + 'Timestamp: {}'.format(self.timestamp))
		print(tabs + 'Input: {}'.format(self.inputs))
		print(tabs + 'Output: {}'.format(self.outputs))