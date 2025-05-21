from stats import num_words
from stats import count_characters
from stats import sort_dictionary
import sys

if(len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    nums = num_words(get_book_text(sys.argv[1]))
    char_dict = count_characters(get_book_text(sys.argv[1]))
    sort_char_dict = sort_dictionary(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {nums} total words")
    print("--------- Character Count -------")
    for dict in sort_char_dict:
        print(f"{dict['char']}: {dict['num']}")

if __name__ == "__main__":
    main()