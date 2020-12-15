from .Transaction import Transaction
from .Block import Block

class Blockchain:

	block_reward = 100
	
	def __init__(self):
		self.blockchain = []
		self.unconfirmed_transactions = []

	def mine_genesis_block(self, miner):
		# add miner rewards
		rewards = Blockchain.block_reward
		reward_transaction = Transaction.create_reward_transaction(miner, rewards)
		self.unconfirmed_transactions.insert(0, reward_transaction)
		# there is no previous block for genesis block
		previous_block = None
		# generate new block from unconfirmed transactions
		new_block = Block(self.unconfirmed_transactions, previous_block)
		# clear unconfirmed transactions
		self.unconfirmed_transactions = []
		# add the new block to blockchain
		self.blockchain.append(new_block)

	def add_transaction(self, transaction):
		# verify if transaction is valid
		if transaction.verify() == True:
			# add new transaction to unconfirmed transactions
			self.unconfirmed_transactions.append(transaction)

	def mine_block(self, miner):
		# add miner rewards
		rewards = Blockchain.block_reward
		reward_transaction = Transaction.create_reward_transaction(miner, rewards)
		self.unconfirmed_transactions.insert(0, reward_transaction)
		# get previous block
		previous_block = self.blockchain[-1]
		# generate new block from unconfirmed transactions
		new_block = Block(self.unconfirmed_transactions, previous_block)
		# clear unconfirmed transactions
		self.unconfirmed_transactions = []
		# add the new block to blockchain
		self.blockchain.append(new_block)

	def print(self):
		print('Blockchain (Blocks count: {})'.format(len(self.blockchain)))
		for block in self.blockchain:
			block.print()