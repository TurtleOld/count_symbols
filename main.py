from collections import Counter


def count_symbols(string):
    lower_string = string.lower()
    dictionary = Counter(lower_string)
    return max(dictionary, key=dictionary.get), max(dictionary.values())
