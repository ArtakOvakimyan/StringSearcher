import tracemalloc


class decorator:
    def measure_memory(func):
        def wrapper(arg):
            tracemalloc.start()
            a = func(arg)
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {current} Bytes")
            tracemalloc.stop()
            return a
        return wrapper
