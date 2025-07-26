def getElement(element: str, size: int):
    """Return list of words superior in size from size"""
    words = element.split(" ")
    is_longer = lambda word, sz: len(word) > sz
    return [w for w in words if is_longer(w, size)]
