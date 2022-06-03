import argparse
from algorithms_handler import Handler
from text import String


def main():
    parser = argparse.ArgumentParser(
        usage="$ python3 [Main-text file_name] {SCRIPT file_name}",
        description="""This script will provide you to compare different methods of searching a substring.
                        The result will be shown on your terminal screen.
                        
                        To start to use:
                            1)Print your text or main-string in file "in.txt"
                            2)Run script by command in terminal: python3 main.py
                            3)Print substring in terminal
                     """
    )
    parser.add_argument("file_path", type=str)
    args = parser.parse_args()
    h = Handler(args.file_path, String(input("Введите подстроку: ")))
    h.perform_all()


if __name__ == "__main__":
    main()

