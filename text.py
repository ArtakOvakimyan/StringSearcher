class main_text(str):
    def __new__(cls):
        value = read_file("in.txt")
        obj = super().__new__(cls, value)
        return obj

    def compare(self, sub_string:str, i: int):
        """Посимвольное сравнение шаблона с частью строки"""
        flag = True
        for j in range(len(str(sub_string))):
            if self[i + j] != str(sub_string)[j]:
                flag = False
                break
        return flag


def read_file(name):
    """Чтение файла с текстом"""
    with open(name, "r") as file:
        text = file.readlines()
    return " ".join(text)


class string(str):
    def __new__(cls, value):
        obj = super().__new__(cls, value)
        return obj
