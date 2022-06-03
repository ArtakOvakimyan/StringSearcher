__all__ = ['KnuthMorrisPratt']
from decorator import decorator


class KnuthMorrisPratt:
    """Алгоритм Кнута-Морриса-Пратта"""
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.lps = self.lps()

    @decorator.measure_memory
    def search(self):
        match_indices = []

        pattern_ind = 0
        for i, ch in enumerate(self.text):
            while pattern_ind and self.pattern[pattern_ind] != ch:
                pattern_ind = self.lps[pattern_ind - 1]

            if self.pattern[pattern_ind] == ch:
                if pattern_ind == self.m - 1:
                    match_indices.append(i - pattern_ind)
                    pattern_ind = self.lps[pattern_ind]
                else:
                    pattern_ind += 1
        return match_indices

    def lps(self):
        array = [0] * self.m
        prefix = 0
        for i in range(1, self.m):
            while prefix and self.pattern[i] != self.pattern[prefix]:
                prefix = array[prefix - 1]
            if self.pattern[prefix] == self.pattern[i]:
                prefix += 1
                array[i] = prefix
        return array
