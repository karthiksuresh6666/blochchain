import hashlib


class RebelCoinGenesisBlock:

    def __init__(self, transaction_list):
        self.transaction_list = transaction_list

        self.data_block = "".join(transaction_list)
        self.block_hash = hashlib.sha256(self.data_block.encode()).hexdigest()
