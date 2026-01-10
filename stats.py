def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars(text):
    char_count = dict()

    for i in text.lower():
        if i in char_count:
            char_count[i] += 1

        else:
            char_count[i] = 1

    return char_count


def char_list(char_count):
    list_count = list()

    for char, count in char_count.items():
        temp = {"char": char, "num": count}
        list_count.append(temp)

    list_count.sort(reverse=True, key=sort_on)

    return list_count


def sort_on(items):

    return items["num"]
