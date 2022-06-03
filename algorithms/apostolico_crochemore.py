__all__ = ['ApostolicoCrochemore']
from decorator import decorator


class ApostolicoCrochemore:
    """Алгоритм Апостолико-Крочемор"""
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.t = self.get_t()

    @decorator.measure_memory
    def search(self):
        indexes = []

        l = 1
        while self.pattern[l - 1] == self.pattern[l]:
            l += 1
        if l == self.m:
            l = 0

        i = l
        j = k = 0
        while j <= (self.n - self.m):
            while i < self.m and self.pattern[i] == self.text[i + j]:
                i += 1
            if i >= self.m:
                while k < l and self.pattern[k] == self.text[j + k]:
                    k += 1
                if k >= l:
                    indexes.append(j)

            j += i - self.t[i]
            if i == l:
                k = max(0, k - 1)
            elif self.t[i] <= l:
                k = max(0, self.t[i])
                i = l
            else:
                k = l
                i = self.t[i]
        return indexes

    def get_t(self):
        i = 0
        t = [0] * (self.m + 1)
        j = t[0] = -1

        while i < self.m:
            while j > -1 and self.pattern[i] != self.pattern[j]:
                j = t[j]
            i += 1
            j += 1
            if i < self.m and self.pattern[i] == self.pattern[j]:
                t[i] = t[j]
            else:
                t[i] = j
        return t

