from datetime import datetime
from hashlib import sha256

class Block:

	def __init__(self, transactions, previous_block):
		if previous_block is None:
			# genesis block
			self.previous_hash = '0'
			self.index = 0

		else:
			# all other blocks
			self.previous_hash = previous_block.hash
			self.index = previous_block.index + 1

		# init block data
		self.timestamp = datetime.now()
		self.transactions = transactions

		# generate block hash
		self.hash = self.generate_hash()

	@staticmethod
	def generate_genesis_block():
		# no transactions and no previous block
		transactions = []
		previous_block = None

		# gen block
		genesis_block = Block(transactions, previous_block)
		return genesis_block

	def generate_hash(self):
		block_data = self.previous_hash + str(self.index) + str(self.timestamp) + str(self.transactions)
		block_hash = sha256(block_data.encode())
		return block_hash.hexdigest()

	def print(self):
		print('Block {}: {}'.format(self.index, self.hash))
		print('Previous hash: {}'.format(self.previous_hash))
		print('Timestamp: {}'.format(self.timestamp))
		print('Transactions count: {}'.format(len(self.transactions)))
		print('Transactions:')
		for transaction in self.transactions:
			transaction.print(tab_count=1)