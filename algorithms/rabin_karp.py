__all__ = ['RabinKarp']
import math
from decorator import decorator
from text import MainText


class RabinKarp:
    def __init__(self, text, pattern):
        """Алгоритм Рабина-Карпа"""
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.hash_str = 0
        self.substr_hash = 0

    @decorator.measure_memory
    def search(self):
        indexes = []

        for i in range(self.m):
            self.substr_hash += math.pow(ord(self.pattern[i]), 2)
            self.hash_str += math.pow(ord(self.text[i]), 2)

        for i in range(self.n - self.m + 1):
            if self.hash_str == self.substr_hash:
                if MainText.compare(self.text, self.pattern, i):
                    indexes.append(i)
            self.hash_str += math.pow(ord(self.text[(i + self.m) % self.n]), 2)
            self.hash_str -= math.pow(ord(self.text[i]), 2)
        return indexes
