def count_words(text):
    return len(text.split())


def count_chars(text):
    lower_case_str = text.lower()
    char_frequency = {}
    for char in lower_case_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency


def sort_on(items):
    return items["num"]


def sorted_dict(items):
    sort_list = []
    for key, val in items.items():
        sort_list.append({"char": key, "num": val})
    sort_list.sort(key=sort_on, reverse=True)
    return sort_list
