from RebelCoin.RebelCoinGenesisBlock import RebelCoinGenesisBlock
from RebelCoin.RebelCoinBlock import RebelCoinBlock


class Transactions:
    t1 = "GOI sends 1000 to K"
    t2 = "K sends 500 to S"
    t3 = "K sends 250 to ICICI"

    initial_block = RebelCoinGenesisBlock([t1])

    print(initial_block.data_block)
    print(initial_block.block_hash)

    first_transaction = RebelCoinBlock(initial_block.block_hash, [t2])

    print(first_transaction.data_block)
    print(first_transaction.block_hash)
