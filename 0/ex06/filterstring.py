import sys

def getElement(element: str, size: int):
    """Return list of words superior in size from size"""
    words = element.split(" ")
    is_longer = lambda word, sz: len(word) > sz
    return [w for w in words if is_longer(w, size)]

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
