from datetime import datetime
from hashlib import sha256

# Create a class Block containing ... transaction...timestamp...previous_hash...nonce...hash
class Block:

    # initialize the instance and  transactions, previous_hash
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    # Generating the hash of the block...which is containing timestamp, transactions, nonce and previous_hash..
    def generate_hash(self):
        block_header = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        
        return block_hash.hexdigest()

    # Printing out the contents in the block....
    def print_contents(self):
        print("Timestamp :", self.timestamp)
        print("Transactions :", self.transactions)
        print("Previous_hash :", self.previous_hash)
        print("Current_hash :", self.hash)