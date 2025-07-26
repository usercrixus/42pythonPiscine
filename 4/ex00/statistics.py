def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        print("Error")
        return
    mid = n // 2
    if n % 2 == 0:
        result = (data[mid - 1] + data[mid]) / 2
    else:
        result = data[mid]
    print(f"median: {result}")


def quartile(data):
    if not data:
        print("Error")
        return
    data = sorted(data)
    n = len(data)
    q1 = data[n // 4]
    q3 = data[3 * (n // 4)]
    print(f"quartile: [{q1}, {q3}]")


def mean(data):
    if not data:
        print("Error")
        return
    result = sum(data) / len(data)
    print(f"mean: {result}")


def std(data):
    if not data:
        print("Error")
        return
    m = sum(data) / len(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    print(f"std: {variance ** 0.5}")


def var(data):
    if not data:
        print("Error")
        return
    m = sum(data) / len(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    print(f"var: {variance}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    availableStat = {"median": median, "quartile": quartile, "mean": mean, "std": std, "var": var}
    try:
        tab = [float(x) for x in args]
    except ValueError:
        print("Error: all arguments must be numbers")
        return

    for key, stat_name in kwargs.items():
        if stat_name in availableStat:
            availableStat[stat_name](tab)
