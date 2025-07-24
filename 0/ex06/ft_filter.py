def ft_filter(myfunc, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    return [x for x in iterable if myfunc(x)]
