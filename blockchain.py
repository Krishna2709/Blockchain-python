from block import Block

# Creating a Blockchain class.....containing initializing, genesis_block, print_block, add_block, validate_block and POW methods...
class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    # Generating a genesis block...
    def genesis_block(self):
        transactions = []
        previous_hash = 0
        genesis_block = Block(transactions, previous_hash)
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    # Adding the block to the blockchain...
    def add_block(self, transactions):
        # find the previuos hash from the chain..
        previous_hash = (self.chain[len(self.chain)-1]).hash
        # initialize the new block
        new_block = Block(transactions, previous_hash)
        # generate the new block's hash
        new_block.generate_hash()
        # proof of work for appending the new block into the chain...
        #proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        #return proof, new_block
        return new_block

    # printing the blocks...
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            # printing out the block contents...
            current_block.print_contents()

    # proof of work...
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while(proof[:difficulty] != 0*difficulty):
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof

    # Validating the chain ...

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if(current_block.hash != current_block.generate_hash()):
                print("The current hash of the block does not equal the generated hash of the block.")
                return False
            if(previous_block.hash != previous_block.generate_hash()):
                print("The previous block's hash does not equal the previous hash value stored in the current block.")
                return False
        return True