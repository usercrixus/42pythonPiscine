def getShape(obj: list):
    "return the array shape, -1 for error"
    if (len(obj) == 0):
        return -1
    shape = len(obj[0])
    for element in obj:
        if (len(element) != shape):
            return -1
    return (len(obj), shape)


def slice_me(family: list, start: int, end: int) -> list:
    "slice a list"
    if (type(family) is not list):
        raise Exception("family isnt of type list")
    shape = getShape(family)
    if (shape[1] == -1):
        raise Exception("Error in the shape of the list")
    else:
        if (start + end > shape[0]):
            raise Exception("can't slice the shape. Out of bound")
        else:
            print(f"My shape is : {shape}")
            newElement = family[start:end]
            shape = getShape(newElement)
            print(f"My new shape is : {shape}")
            return newElement
