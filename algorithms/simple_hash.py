__all__ = ['SimpleHash']
from decorator import decorator
from text import MainText


class SimpleHash:
    """Алгоритм сравнения по сумме хэш-кодов"""
    def __init__(self, text, pattern):
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
            self.substr_hash += ord(self.pattern[i])
            self.hash_str += ord(self.text[i])

        for i in range(self.n - self.m + 1):
            if self.hash_str == self.substr_hash:
                if MainText.compare(self.text, self.pattern, i):
                    indexes.append(i)
            self.hash_str += ord(self.text[(i + self.m) % self.n]) - ord(self.text[i])
        return indexes
