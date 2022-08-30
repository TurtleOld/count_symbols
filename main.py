from collections import Counter


def count_symbols(string):
    lower_string = string.lower()
    count = Counter(lower_string)
    return max(count, key=count.get), max(count.values())
