# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

It’s a simple command-line tool that analyzes a text file (a book) and prints some basic statistics.

## What it does

- Reads a book text file from a path you provide
- Counts the total number of words
- Counts how many times each character appears
- Prints a formatted report of the most common letters

## How to run

1. Make sure you have Python 3 installed.
2. From the project directory, run:

```bash
python3 main.py <path_to_book>

For example:
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt

If you run it without a book path, you’ll see a helpful usage message:
python3 main.py
# Usage: python3 main.py <path_to_book>

Project goals
Practice reading files from disk
Work with functions and modules
Use command-line arguments (sys.argv)
Practice basic text and frequency analysis
