class MainText:
    def __init__(self, name: str):
        self.value = self.read_file(name)

    @staticmethod
    def compare(string: str, sub_string: str, i: int) -> bool:
        """Посимвольное сравнение шаблона с частью строки"""
        for j in range(len(str(sub_string))):
            if string[i + j] != str(sub_string)[j]:
                return False
        return True

    def read_file(self, name: str):
        """Чтение файла с текстом"""
        with open(name, "r") as file:
            text = file.readlines()
        return " ".join(text)

    def get_string(self) -> str:
        return self.value


class String(str):
    def __new__(cls, value):
        obj = super().__new__(cls, value)
        return obj
