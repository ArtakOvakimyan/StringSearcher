import time

import algorithms
from text import MainText


class Handler:
    def __init__(self, path: str, sub_string: str):
        self.text = MainText(path).get_string()
        self.sub_string = sub_string
        self.algorithms = [(f, name) for name, f in algorithms.__dict__.items() if callable(f)]

    def perform(self, method, name: str):
        """Исполнение алгоритма, отчёт времени"""
        in_time = time.time()
        result = method(self.text, self.sub_string).search()
        print("Function Name: {0}".format(name))
        res_time = time.time() - in_time
        print("Time used: {0} seconds".format(res_time), "\nindexes: ", result, "\n")

    def perform_all(self):
        for f, name in self.algorithms:
            self.perform(f, name)
