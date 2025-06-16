import sys
from stats import *

def get_book_text(relative_path):
    with open(relative_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = get_word_count(text)
    character_count = sort_character_count(get_character_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in character_count:
        print(f"{char['character']}: {char['count']}")
    print("============= END ===============")

main()