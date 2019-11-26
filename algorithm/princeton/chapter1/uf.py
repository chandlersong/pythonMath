import numpy as np


class UF:
    def __init__(self, n: int):
        self.__id = np.arange(n)
        self.__count = n

    def union(self, p: int, q: int):
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id == q_id:
            return

        for i in range(0, len(self.__id)):
            if self.__id[i] == p_id:
                self.__id[i] = q_id
        self.__count = self.__count - 1

    def find(self, p: int) -> int:
        return self.__id[p]

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    @property
    def count(self) -> int:
        return self.__count

    @property
    def id(self) -> np.array:
        return self.__id
