#!/usr/bin/env python3

from src.Wallet import Wallet
from src.Transaction import Transaction
from src.Blockchain import Blockchain

blockchain = Blockchain()

alice_wallet = Wallet('Alice')
bob_wallet = Wallet('Bob')
charlie_wallet = Wallet('Charlie')
david_wallet = Wallet('David')

blockchain.add_transaction(Transaction(alice_wallet, bob_wallet, 100))
blockchain.add_transaction(Transaction(bob_wallet, charlie_wallet, 20))
blockchain.mine_block(alice_wallet)
blockchain.add_transaction(Transaction(david_wallet, charlie_wallet, 50))
blockchain.mine_block(alice_wallet)
blockchain.mine_block(charlie_wallet)
blockchain.add_transaction(Transaction(charlie_wallet, alice_wallet, 200))
blockchain.add_transaction(Transaction(alice_wallet, david_wallet, -10))
blockchain.mine_block(alice_wallet)

blockchain.print()