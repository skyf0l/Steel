#!/usr/bin/env python3

from src.Transaction import Transaction
from src.Blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_transaction(Transaction("Alice", "Bob", 100))
blockchain.add_transaction(Transaction("Bob", "Charlie", 20))
blockchain.mine_block()
blockchain.add_transaction(Transaction("David", "Charlie", 50))
blockchain.mine_block()
blockchain.mine_block()
blockchain.add_transaction(Transaction("Charlie", "Alice", 200))
blockchain.add_transaction(Transaction("Alice", "David", 10))
blockchain.mine_block()

blockchain.print()