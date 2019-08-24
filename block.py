'''
Author: Junior Masilela 
Project Description:  Building blocks for blockchain 

'''

from hashlib import sha256
from datetime import datetime 

class Block: 

    '''
    This class initiates the structure of the Block.
    
    Arguments: 

    :timestamp:     Current time of the entry to keep track of the sequencing of the blocks
    :transactions:  Record of each transaction (symbolic reference for the data being transferred)
    :previous_hash: The last block of the blockchain, this acts as a reference point for where the next block should be placed 
    :nonce: 
    :hash:          The encrypted output of the transaction (through the sha256 function)
    '''

    def __init__(self, transactions, 
    previous_hash, nonce=0): 
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self): 
        ''' 
        Prints the contents within the block
        '''

        print("timestamp: ", self.timestamp)
        print("transactoins: ", self.transactions)
        print(" previous hash: ", self.previous_hash)
        print("current hash: ", self.hash)

    def generate_hash(self):
        '''
       Function to hash the block contents using the sha256 algorithm 
       then return the output 
        '''

        block_contents= str(self.timestamp) + str(self.transactions)
        + str(self.previous_hash) + str(self.nonce) 

        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()



        