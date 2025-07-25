from filterstring import getElement
import sys

if __name__ == "__main__":
    arg = sys.argv[1:]  # Exclude the program name
    if len(arg) != 2:
        print("AssertionError")
    else:
        try:
            s = arg[0]
            n = int(arg[1])
            print(getElement(s, n))
        except ValueError:
            print("AssertionError")
