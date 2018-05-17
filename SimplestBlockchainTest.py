#This program is freely inspired from CryptoCurrently's medium post: https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

import hashlib as hasher

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
        
import datetime as date

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")
    
    
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "This is block " + str(this_index)
    this_hash = last_block.hash
    
    return Block(this_index, this_timestamp, this_data, this_hash)
    
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

number_of_blocks_to_add = 50

for i in range(1, number_of_blocks_to_add + 1):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    
    print ("Block #" + str(block_to_add.index) + " has been added to the bloackchain")
    print("Timestamp: " + str(block_to_add.timestamp))
    print("Data: " + block_to_add.data)
    print("Previous hash: " + block_to_add.previous_hash)
    print("Hash: " + block_to_add.hash)
    print()
    
    