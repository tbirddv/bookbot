import shutil
def main():

    book = input("Enter the name of the book: ")

    if not book:
        print("Error: You didn't enter a book. Defaulting to frankenstein")
        book = "frankenstein"
    
    book, file_contents = read_book_file(book)
    num_words = word_count(file_contents)
    letter_counts = character_count(file_contents)
    
    return book, num_words, letter_counts
    
def print_results():
    book, num_words, letter_counts = main() 
    terminal_width = shutil.get_terminal_size().columns
    padding = terminal_width // 8
       
    print("\nLetter counts will be printed alphabetically by default.\n")
    by_count = input("Do you want to print the letter counts by count? (y/n): ") 
    print("\n")

    print("- - - - - Begin Report - - - - -".center(terminal_width))
    print(f"Title: {book.upper()}".center(terminal_width))
    print("\n")
    print(" " * padding + f"Number of words: {num_words}")
    print("\n")
    print(" " * padding + "The letter counts are:")
    if by_count.lower() == "y":
        for letter, count in sorted(letter_counts.items(), key=lambda x: x[1], reverse=True):
            print(" " * (padding + (padding // 2)) + f"{letter}: {count}")
    else:
        for letter, count in sorted(letter_counts.items()):
            print(" " * (padding + (padding // 2)) + f"{letter}: {count}")
    print("- - - - - End Report - - - - -".center(terminal_width))

def read_book_file(book):
    try:
        with open(f"books/{book}.txt") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The book '{book}' does not exist. Defaulting to 'frankenstein'.")
        book = "frankenstein"
        try:
            with open("books/frankenstein.txt") as f:
                file_contents = f.read()
        except FileNotFoundError:
            print("Error: The default book 'frankenstein' does not exist. Exiting.")
            exit(1)
    return book, file_contents

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    counts = {}
    lower_case_string = file_contents.lower()
    for char in lower_case_string:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

print_results()
