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
