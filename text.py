class main_text():
    def __init__(self, file_name):
        self.string = read_file(file_name)

    def compare(self, sub_string:str, i: int):
        """Посимвольное сравнение шаблона с частью строки"""
        flag = True
        for j in range(len(str(sub_string))):
            if self.string[i + j] != str(sub_string)[j]:
                flag = False
                break
        return flag


def read_file(name):
    """Чтение файла с текстом"""
    with open(name, "r") as file:
        text = file.readlines()
    return " ".join(text)


class string(str):
    def __init__(self):
        self.input = input("Введите подстроку: ")
