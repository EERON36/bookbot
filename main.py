from stats import get_num_words, get_chars, sort_on


def get_book_text(file_path):
    # Take file path as input and return text as string
    # open file
    with open(file_path) as f:

        # read file
        file_contents = f.read()

    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars(text)
    # print(f"Found {num_words} total words")
    # print(chars)
    list_nums = sort_on(chars)
    print(list_nums)


main()
