__all__ = ['ZSearch']
from decorator import decorator


class ZSearch:
    """Алгоритм с вычислением Z-функции"""
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.m = len(pattern)
        self.n = len(text)
        self.z_value = self.z_function(self.pattern + self.text)

    @decorator.measure_memory
    def search(self):
        answers = []
        for (i, val) in enumerate(self.z_value):
            if val >= self.m:
                answers.append(i - self.m)
        return answers

    def z_function(self, string):
        z_result = [0] * len(string)

        left_pointer, right_pointer = 0, 0

        for i in range(1, len(string)):
            if i <= right_pointer:
                min_edge = min(right_pointer - i + 1, z_result[i - left_pointer])
                z_result[i] = min_edge

            while i + z_result[i] < len(string) and string[z_result[i]] == string[i + z_result[i]]:
                z_result[i] += 1

            if i + z_result[i] - 1 > right_pointer:
                left_pointer, right_pointer = i, i + z_result[i] - 1
        return z_result
