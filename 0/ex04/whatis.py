import sys

def even(number):
    if (number % 2 == 0):
        print("I'm even")
    else:
        print("I'm odd")


if __name__ == "__main__":
    arg = sys.argv
    if (len(arg) > 2):
        print("AssertionError: more than one argument is provided")
    elif (len(arg) == 2):
        try:
            value = int(arg[1])
            even(value)
        except ValueError:
            print("AssertionError: argument is not an integer")
