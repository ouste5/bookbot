import sys
from codecs import ignore_errors
from dataclasses import replace

from stats import count_words, number_words, sorted_list


def get_book_text(input_file):
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    word_count = count_words(get_book_text(book_path))
    chars_dict = number_words(get_book_text(book_path))
    chars_sorted_list = sorted_list(chars_dict)
    print_report(book_path, word_count, chars_sorted_list)

def print_report(book_path, num_words, chars_sorted_list):
    print("===========BOOKBOT===========")
    print(f"Analyzing book found at {book_path}...")
    print("----------Word Count----------")
    print(f"Found {num_words} total words")
    print("----------Character Count----------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("=========== END ===========")


main()