import math
import time
from memory_profiler import profile
from text import main_text, string


class algorithm():
    def __init__(self):
        self.text = main_text()
        self.sub_string = string(input("Введите подстроку: "))
        self.algorithms = [brute_force, boyer_moore_horspool, rabin_karp, simple_hash, square_hash, kmp]

    def perform(self, method):
        """Исполнение алгоритма, отчёт времени"""
        in_time = time.time()
        result = method(self.text, self.sub_string)
        res_time = time.time() - in_time
        print("time used for {0}: {1} ".format(method.__name__, res_time), "\nindexes: ", result)

    def perform_all(self):
        for e in self.algorithms:
            self.perform(e)


@profile
def brute_force(text, pattern):
    """Грубый поиск подстроки в строке """
    indexes = list()
    for i in range(len(text) - len(pattern)):
        if text.compare(pattern, i):
            indexes.append(i)
    return indexes


@profile
def boyer_moore_horspool(text, pattern):
    """Алгоритм Бойера-Мура-Хорспула"""
    m = len(pattern)
    n = len(text)
    skip = {}
    found_indexes = []

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)
        if ord(text[k]) in skip:
            k += skip[ord(text[k])]
        else:
            skip[ord(text[k])] = m
            k += m

    return found_indexes


@profile
def rabin_karp(text, pattern):
    """Алгоритм Рабина-Карпа"""
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(pattern)):
        substr_hash += ord(pattern[i]) * math.pow(2, len(pattern) - i - 1)
        hash_str += ord(text[i]) * math.pow(2, len(pattern) - i - 1)

    for i in range(len(text) - len(pattern)):
        if hash_str == substr_hash:
            if text.compare(pattern, i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str -= ord(text[i]) * math.pow(2, len(pattern) - 1)
        hash_str *= 2
        hash_str += ord(text[i + len(pattern)])
    print("RabinKarp collisions:", collisions)
    return indexes


@profile
def simple_hash(text, pattern):
    """Алгоритм сравнения по сумме хэш-кодов"""
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(pattern)):
        substr_hash += ord(pattern[i])
        hash_str += ord(text[i])

    for i in range(len(text) - len(pattern)):
        if hash_str == substr_hash:
            if text.compare(pattern, i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str += ord(text[i + len(pattern)]) - ord(text[i])
    print("SimpleHash collisions:", collisions)
    return indexes


@profile
def square_hash(text, pattern):
    """Алгоритм сравнения по сумме квадратов хэш-кодов"""
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(pattern)):
        substr_hash += math.pow(ord(pattern[i]), 2)
        hash_str += math.pow(ord(text[i]), 2)

    for i in range(len(text) - len(pattern)):
        if substr_hash == hash_str:
            if text.compare(pattern, i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str += math.pow(ord(text[i + len(pattern)]), 2) - math.pow(
            ord(text[i]), 2
        )
    print("SquareHash collisions:", collisions)
    return indexes


@profile
def kmp(text, pattern):
    """Алгоритм Кнута-Морриса-Пратта"""
    match_indices = []
    pattern_lps = lps(pattern)

    pattern_ind = 0
    for i, ch in enumerate(text):
        while pattern_ind and pattern[pattern_ind] != ch:
            pattern_ind = pattern_lps[pattern_ind - 1]

        if pattern[pattern_ind] == ch:
            if pattern_ind == len(pattern) - 1:
                match_indices.append(i - pattern_ind)
                pattern_ind = pattern_lps[pattern_ind]
            else:
                pattern_ind += 1
    return match_indices


def lps(pattern):
    array = [0] * len(pattern)
    prefix = 0
    for i in range(1, len(pattern)):
        while prefix and pattern[i] != pattern[prefix]:
            prefix = array[prefix - 1]
        if pattern[prefix] == pattern[i]:
            prefix += 1
            array[i] = prefix
    return array
