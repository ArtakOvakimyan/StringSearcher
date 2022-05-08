import math
import time
from memory_profiler import profile
from text import main_text, string


class algorithm():
    def __init__(self):
        self.text = main_text("in.txt")
        self.algorithms = [brute_force, boyer_moore_horspool, rabin_karp, simple_hash, square_hash]

    def perform(self, method):
        """Исполнение алгоритма, отчёт времени"""
        in_time = time.time()
        result = method(self.text)
        res_time = time.time() - in_time
        print("time used for {0}: {1} ".format(method.__name__, res_time), "\nindexes: ", result)

    def perform_all(self):
        for e in self.algorithms:
            self.perform(e)


@profile
def brute_force(text):
    """Грубый поиск подстроки в строке """
    indexes = list()
    for i in range(len(text.string) - len(string().input)):
        if text.compare(string, i):
            indexes.append(i)
    return indexes


@profile
def boyer_moore_horspool(text):
    """Алгоритм Бойера-Мура-Хорспула"""
    m = len(str(string))
    n = len(text.string)

    skip = {}
    found_indexes = []

    for k in range(m - 1):
        skip[ord(str(string)[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text.string[i] == str(string)[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)
        if ord(text.string[k]) in skip:
            k += skip[ord(text.string[k])]
        else:
            skip[ord(text.string[k])] = m
            k += m

    return found_indexes


@profile
def rabin_karp(text):
    """Алгоритм Рабина-Карпа"""
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(str(string))):
        substr_hash += ord(str(string)[i]) * math.pow(2, len(str(string)) - i - 1)
        hash_str += ord(text.string[i]) * math.pow(2, len(str(string)) - i - 1)

    for i in range(len(text.string) - len(str(string))):
        if hash_str == substr_hash:
            if text.compare(str(string), i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str -= ord(text.string[i]) * math.pow(2, len(str(string)) - 1)
        hash_str *= 2
        hash_str += ord(text.string[i + len(str(string))])
    print("RabinKarp collisions:", collisions)
    return indexes


@profile
def simple_hash(text):
    """Алгоритм сравнения по сумме хэш-кодов"""
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(str(string))):
        substr_hash += ord(str(string)[i])
        hash_str += ord(text.string[i])

    for i in range(len(text.string) - len(str(string))):
        if hash_str == substr_hash:
            if text.compare(str(string), i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str += ord(text.string[i + len(str(string))]) - ord(text.string[i])
    print("SimpleHash collisions:", collisions)
    return indexes


@profile
def square_hash(text):
    """Алгоритм сравнения по сумме квадратов хэш-кодов"""
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(str(string))):
        substr_hash += math.pow(ord(str(string)[i]), 2)
        hash_str += math.pow(ord(text.string[i]), 2)

    for i in range(len(text.string) - len(str(string))):
        if substr_hash == hash_str:
            if text.compare(i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str += math.pow(ord(text.string[i + len(str(string))]), 2) - math.pow(
            ord(text.string[i]), 2
        )
    print("SquareHash collisions:", collisions)
    return indexes
