import hashlib
import time

# Step 1: Define the Block class
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions  # List of payment transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Creates a SHA-256 hash of the block's contents.
        """
        block_string = str(self.index) + str(self.transactions) + str(self.timestamp) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

# Step 2: Define the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 6  # Number of leading zeros required in hash
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the first block in the chain (genesis block).
        """
        genesis_block = Block(0, [], time.time(), "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        """
        Adds a new transaction to the list of pending transactions.
        """
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.pending_transactions.append(transaction)

    def proof_of_work(self, block):
        """
        Simple proof-of-work algorithm: find a hash with leading zeros.
        """
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block.hash

    def mine_pending_transactions(self):
        """
        Mines a block containing all pending transactions.
        """
        if not self.pending_transactions:
            return False

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            timestamp=time.time(),
            previous_hash=self.get_last_block().hash
        )

        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear after mining
        return new_block

    def is_chain_valid(self):
        """
        Validates the blockchain's integrity.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

# Step 3: Simulate payments
my_blockchain = Blockchain()

# Add some transactions
my_blockchain.add_transaction("Alice", "Bob", 10)
my_blockchain.add_transaction("Bob", "Charlie", 5)

# Measure total mining time
start_total = time.time()

# Mine the block
mined_block = my_blockchain.mine_pending_transactions()

# Add more transactions
my_blockchain.add_transaction("Charlie", "Alice", 2)
my_blockchain.add_transaction("Alice", "David", 7)

# Mine another block
my_blockchain.mine_pending_transactions()

end_total = time.time()
total_mining_time = end_total - start_total
print(f"\n⏱️ Total mining time: {total_mining_time:.2f} seconds")

# Step 4: Display the blockchain
for block in my_blockchain.chain:
    print(f"Block {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print("-" * 40)

# Step 5: Validate the chain
print("Is blockchain valid?", my_blockchain.is_chain_valid())

