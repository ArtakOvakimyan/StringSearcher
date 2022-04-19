import threading
import time
import argparse
import math
from collections import defaultdict

from memory_profiler import profile


string, subString = "", ""


def perform(method):
    in_time = time.time()
    result = method()
    res_time = time.time() - in_time
    print("time used for {0}: {1} ".format(method.__name__, res_time), "\nindexes: ", result)


def compare(i):
    flag = True
    for j in range(len(subString)):
        if string[i + j] != subString[j]:
            flag = False
            break
    return flag


@profile
def brute_force():
    indexes = list()
    for i in range(len(string) - len(subString)):
        if compare(i):
            indexes.append(i)
    return indexes

@profile
def boyer_moore_horspool():
    m = len(subString)
    n = len(string)

    if m > n:
        return -1

    skip = defaultdict(lambda: m)
    found_indexes = []

    for k in range(m - 1):
        skip[ord(subString[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and string[i] == subString[j]:
            j -= 1
            i -= 1
        if j == -1:
            found_indexes.append(i + 1)

        k += skip[ord(string[k])]

    return found_indexes


@profile
def rabin_karp():
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(subString)):
        substr_hash += ord(subString[i]) * math.pow(2, len(subString) - i - 1)
        hash_str += ord(string[i]) * math.pow(2, len(subString) - i - 1)

    for i in range(len(string) - len(subString)):
        if hash_str == substr_hash:
            if compare(i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str -= ord(string[i]) * math.pow(2, len(subString) - 1)
        hash_str *= 2
        hash_str += ord(string[i + len(subString)])
    print("RabinKarp collisions:", collisions)
    return indexes


@profile
def simple_hash():
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(subString)):
        substr_hash += ord(subString[i])
        hash_str += ord(string[i])

    for i in range(len(string) - len(subString)):
        if hash_str == substr_hash:
            if compare(i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str += ord(string[i + len(subString)]) - ord(string[i])
    print("SimpleHash collisions:", collisions)
    return indexes


@profile
def square_hash():
    indexes = []
    hash_str = 0
    substr_hash = 0
    collisions = 0
    for i in range(len(subString)):
        substr_hash += math.pow(ord(subString[i]), 2)
        hash_str += math.pow(ord(string[i]), 2)

    for i in range(len(string) - len(subString)):
        if substr_hash == hash_str:
            if compare(i):
                indexes.append(i)
            else:
                collisions += 1
        hash_str += math.pow(ord(string[i + len(subString)]), 2) - math.pow(
            ord(string[i]), 2
        )
    print("SquareHash collisions:", collisions)
    return indexes


def read_file(name):
    with open(name, "r") as file:
        text = file.readlines()
    return " ".join(text)


def main():
    global subString, string
    parser = argparse.ArgumentParser(
        usage="python3 {SCRIPT file_name} [MAIN-TEXT file_name] [SUBSTRING TEXT file_name] [METHOD name]",
        description="This script will provide you to compare different methods of searching a substring in a text on "
        "various texts. The result will be shown on your terminal screen :)",
    )
    parser.add_argument("main", type=str)
    args = parser.parse_args()
    string = read_file(args.main)
    subString = input("Введите подстроку: ")

    methods = [brute_force, boyer_moore_horspool, rabin_karp, simple_hash, square_hash]
    for method in methods:
        perform(method)


if __name__ == "__main__":
    main()
