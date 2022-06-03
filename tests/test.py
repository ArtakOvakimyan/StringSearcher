import unittest
import algorithms
from text import MainText


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.algorithms = [(f, name) for name, f in algorithms.__dict__.items() if callable(f)]

    def test1(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test1.txt").get_string(), "sa").search(), [3089, 7180])

    def test2(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test2.txt").get_string(), "Павловна").search(),
                             [654, 831, 2405, 3439, 4096, 6948, 7273, 7728, 8293])

    def test3(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test3.txt").get_string(), "сын князя Василия").search(), [599])

    def test4(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test4.txt").get_string(),
            "Да, я слышал про его план вечного мира, и это очень интересно, но едва ли возможно...").search(), [614])

    def test5(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test5.txt").get_string(),
            "людьми, называемыми бесхарактерными, ему так страстно захотелось войти взглянуть ").search(), [1681])

    def test6(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test6.txt").get_string(),
            "Бутылка рому была принесена; раму, не пускавшую сесть на наружный откос окна, выламывал").search(), [9544])

    def test7(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test7.txt").get_string(), "ab").search(), [8])

    def test8(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test8.txt").get_string(), "ab").search(), [98])

    def test9(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test9.txt").get_string(), "ab").search(), [998])

    def test10(self):
        for f, name in self.algorithms:
            self.assertEqual(f(MainText("../templates/test10.txt").get_string(), "ab").search(), [4896, 5014])


if __name__ == "__main__":
    unittest.main()
