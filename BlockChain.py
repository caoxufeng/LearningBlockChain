# -*- coding: utf-8 -*-

import hashlib as hasher
import datetime as data


class Block:
    def __init__(self, index, timestamp, data, previous_hask):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hask = previous_hask
        self.hash = self.hask_block()

    # 生成新的hash
    def hask_block(self):
        sha = hasher.sha256()
        sha.update(
            bytes(
                str(self.index) + str(self.timestamp) +
                str(self.data) + str(self.previous_hask), 'utf-8'
            )
        )
        return sha.hexdigest()


# 生成创世链
def create_genesis_block():
    return Block(0, data.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = data.datetime.now()
    this_data = "Hey! I'm block" + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


def main():
    # create the blockchain and add the genensis.
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    # 创世链之后酱油多少个Block被添加
    num_of_blocks_to_add = 20
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)  # 根据上一个Block 生成的下一个区块
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the"
              "blockchain!".format(block_to_add.index))
        print("Hash:{}!\n".format(block_to_add.hash))


if __name__ == "__main__":
    main()
