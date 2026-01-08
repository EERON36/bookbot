def get_book_text(file_path):
    # Take file path as input and return text as string
    # open file
    with open(file_path) as f:

        # read file
        file_contents = f.read()

    return file_contents


def main():
    print(get_book_text("./books/frankenstein.txt"))


main()
