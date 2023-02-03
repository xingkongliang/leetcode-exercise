# <int, float, 3>
# 下面是一个例子(int -> float)，新 -> 旧
# insert(10, 0.1)  // 伪代码，接口
# insert(30, 0.3)
# insert(20, 0.2)
# [20: 0.2, 30: 0.3, 10: 0.1]  // 逻辑上的新旧顺序
# {20: 0.2, 30: 0.3, 10: 0.1}
# get(30) -> 0.3
# [30: 0.3, 20: 0.2, 10: 0.1]  // 重排


class LRU_cache:
    def __init__(self, capacity=3):
        self.cache = dict()
        self.rank = list()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache.keys():
            return False
        self.rank.remove(key)
        self.rank.append(key)
        return self.cache[key]

    def insert(self, key, value):
        if len(self.rank) == self.capacity and key not in self.cache.keys():
            key_pop = self.rank.pop(0)
            del self.cache[key_pop]
        if key in self.cache.keys():
            self.rank.remove(key)
            self.rank.append(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.rank.append(key)
        
S = LRU_cache(capacity=3)
S.insert(10, 0.1)
S.insert(30, 0.3)
S.insert(20, 0.2)
print(S.cache)
print(S.rank)
print("*"*20)
print(S.get(30))
S.insert(40, 0.4)
print(S.cache)
print(S.rank)
print("*"*20)
print(print(S.get(10)))
S.insert(20, 0.25)
print(S.cache)
print(S.rank)
