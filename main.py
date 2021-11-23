# AUTHOR: Gloriel M. Soto Maldonado

from syntax import parser

fileName = "Test.txt"
file = open(fileName, "r")


def main():
    parser.parse(file.read())
    print("Finished.")


if __name__ == '__main__':
    main()
