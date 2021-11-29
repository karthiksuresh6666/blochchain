import hashlib


class RebelCoinBlock:

    def __init__(self, previous_block, transaction_list):
        self.previous_block = previous_block
        self.transaction_list = transaction_list

        self.data_block = previous_block.join(transaction_list)
        self.block_hash = hashlib.sha256(self.data_block.encode()).hexdigest()
