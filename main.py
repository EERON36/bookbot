def get_book_text(file_path):
    # Take file path as input and return text as string
    # open file
    with open(file_path) as f:

        # read file
        file_contents = f.read()

    return file_contents


def count_words(text):
    words = text.split()

    return len(words)


def main():
    # print(get_book_text("./books/frankenstein.txt"))
    message = (
        f"Found {count_words(get_book_text("./books/frankenstein.txt"))} total words"
    )
    print(message)


main()
