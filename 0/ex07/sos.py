import sys


def helper():
    """Help to print morse string"""

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }

    argv = sys.argv
    if (len(argv) != 2):
        print("AssertError: number of arg")
        return (1)
    else:
        for x in argv[1]:
            if (x.upper() not in NESTED_MORSE.keys()):
                print("AssertError: string format")
                return (1)
        else:
            for x in argv[1].upper():
                print(NESTED_MORSE[x], end='')
            print()


if __name__ == "__main__":
    helper()
