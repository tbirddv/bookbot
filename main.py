def main():

    book = input("Enter the name of the book: ")

    if not book:
        print("Error: You didn't enter a book. Defaulting to frankenstein")
        book = "frankenstein"
    
    book, file_contents = get_string(book)

    
    
    num_words = word_count(file_contents)
    
    print(f"The word count of {book} is {num_words}")

def get_string(book):
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
    return (book, file_contents)

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

main()
