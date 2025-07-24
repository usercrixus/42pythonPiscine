import sys

def insight(text:str):
    """give insight on the text passed as argument"""
    upper = 0
    lower = 0
    ponctuation = 0
    digit = 0
    space = 0

    for x in text:
        if (x.isupper()):
            upper += 1
        elif (x.isdigit()):
            digit += 1
        elif (x.islower()):
            lower += 1
        elif (x.isspace()):
            space += 1
        else:
            ponctuation += 1

    print(f"the text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{ponctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")

if __name__ == "__main__":
    argv = sys.argv
    if (len(argv) > 2):
        print("AssertionError")
    elif (len(argv) == 2):
        insight(argv[1])
    else:
        value = input("What is the text to count?")
        insight(value)