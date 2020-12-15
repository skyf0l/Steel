from .Transaction import Transaction
from .Block import Block

class Blockchain:

	block_reward = 100
	
	def __init__(self):
		self.blockchain = []
		self.unconfirmed_transactions = []
		self.add_genesis_block()

	def add_genesis_block(self):
		# generate the genesis block
		genesis_block = Block.generate_genesis_block()
		# add the genesis block to blockchain
		self.blockchain.append(genesis_block)

	def add_transaction(self, transaction):
		# verify if transaction is valid
		if transaction.verify() == True:
			# add new transaction to unconfirmed transactions
			self.unconfirmed_transactions.append(transaction)

	def mine_block(self, miner):
		# add miner rewards
		rewards = Blockchain.block_reward
		self.unconfirmed_transactions.insert(0, Transaction('REWARD', miner, rewards))
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