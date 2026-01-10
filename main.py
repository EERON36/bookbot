import sys
from stats import get_num_words, get_chars, sort_on, char_list


def get_book_text(file_path):
    # Take file path as input and return text as string
    # open file
    with open(file_path) as f:

        # read file
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars(text)
    sorted_chars = char_list(chars)
    # print(f"Found {num_words} total words")
    # print(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {count}")
    print("============= END ===============")


main()
