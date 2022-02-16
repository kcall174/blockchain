#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self, chain = [], all_transactions = []):
      self.chain = chain
      self.all_transactions = all_transactions
    
    
    def genesis_block(self):
      transactions = []
      previous_hash = '0'
      self.chain.append(Block(transactions, previous_hash))
      self.genesis_block()
    
