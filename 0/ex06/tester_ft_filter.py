from ft_filter import ft_filter

def myfilter(element):
    "filter on word o"
    if (element == "o"):
        return False
    else:
        return True

if __name__ == "__main__":
    mystr = "hello to all world !"
    print("".join(ft_filter(myfilter, mystr)))