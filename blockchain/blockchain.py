# import datetime library
from datetime import datetime
# print current date and time
#print(datetime.now())

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
  'receiver': 'Kenneth Calaghan Jr'}

#adding it to the list mempool
mempool.append(my_transaction)


block_transactions = [my_transaction, transaction4, transaction6]
print(block_transactions)



    
    
    
    
    
    
    
    
    
