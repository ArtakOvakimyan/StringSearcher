__all__ = ['Bruteforce']
from decorator import decorator
from text import MainText


class Bruteforce:
    """Грубый поиск подстроки"""
    def __init__(self, text, pattern):
        self.text: MainText = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)

    @decorator.measure_memory
    def search(self):
        indexes = []
        for i in range(self.n - self.m + 1):
            if MainText.compare(self.text, self.pattern, i):
                indexes.append(i)
        return indexes
