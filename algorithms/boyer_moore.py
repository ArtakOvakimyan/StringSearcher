__all__ = ['BoyerMoore']
from collections import defaultdict
from decorator import decorator


class BoyerMoore:
    """Алгоритм Бойера-Мура"""
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.bad_char = self.bad_character()

    @decorator.measure_memory
    def search(self):
        indexes = []
        s = 0
        while s <= self.n - self.m:
            j = self.m - 1
            while j >= 0 and self.pattern[j] == self.text[s + j]:
                j -= 1
            if j < 0:
                indexes.append(s)
                s += (self.m - self.bad_char[ord(self.text[s + self.m])] if s + self.m < self.n else 1)
            else:
                s += max(1, j - self.bad_char[ord(self.text[s + j])])
        return indexes

    def bad_character(self):
        bad_char = defaultdict(lambda: -1)
        for i in range(self.m):
            bad_char[ord(self.pattern[i])] = i
        return bad_char
