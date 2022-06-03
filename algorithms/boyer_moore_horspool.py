__all__ = ['BoyerMooreHorspool']
from decorator import decorator


class BoyerMooreHorspool:
    """Алгоритм Бойера-Мура-Хорспула"""
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)

    @decorator.measure_memory
    def search(self):
        skip = {}
        indexes = []

        for k in range(self.m - 1):
            skip[ord(self.pattern[k])] = self.m - k - 1

        k = self.m - 1

        while k < self.n:
            j = self.m - 1
            i = k
            while j >= 0 and self.text[i] == self.pattern[j]:
                j -= 1
                i -= 1
            if j == -1:
                indexes.append(i + 1)
            if ord(self.text[k]) in skip:
                k += skip[ord(self.text[k])]
            else:
                skip[ord(self.text[k])] = self.m
                k += self.m
        return indexes
