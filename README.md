## basic blockchain example 
### creating Block
```
import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash):
    self.timestamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()
```
### creating Blockchain
```
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.unconfirmed_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = []
    genesis_block = Block(transactions, "0")
    genesis_block.generate_hash()
    self.chain.append(genesis_block)

  def add_block(self, transactions):
    previous_hash = (self.chain[len(self.chain)-1]).hash
    new_block = Block(transactions, previous_hash)
    new_block.generate_hash()
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True
  
  def proof_of_work(self,block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof
```
### script for blockchain 
```
from hashlib import sha256
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()
print(proof)
  
# finding a proof that has 2 leading zeros
while (proof[:2] != '0' * difficulty):
  nonce += 1
  proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)
```
### sha256 hashing 
```
from hashlib import sha256

# text to hash
text = "I am excited to learn about blockchain"
print(text)

hash_result = sha256(text.encode())
print(hash_result.hexdigest())
```
### transaction(s) example
```
from datetime import datetime
from blockchain import Blockchain

class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce=0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.timestamp = datetime.now()

    
transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# my_transaction example
my_transaction = {
  'amount': '25000',
  'sender': 'Universe',
  'receiver': 'kcall174'}

#adding it to the list mempool
mempool.append(my_transaction)


block_transactions = [my_transaction, transaction4, transaction6]
print(block_transactions)

#more transactions, using methods made. 
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()
```



