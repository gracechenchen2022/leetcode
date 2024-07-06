import random

class RandomizedSet:
    def __init__(self):
        self.dict = {}  # 哈希表，用于存储元素及其索引
        self.list = []  # 数组，用于存储元素

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        index = self.dict[val]
        last_element = self.list[-1]

        # 将数组末尾的元素移到被删除元素的位置
        self.list[index] = last_element
        self.dict[last_element] = index

        # 删除数组末尾的元素和哈希表中的对应项
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
