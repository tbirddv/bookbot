def main():

    #Main function to read and print the contents of a book file.

    book = input("Enter the name of the book: ")

    if not book:
        print("Error: You didn't enter a book. I will print frankenstein instead")
        book = "frankenstein"
    try:
        with open(f"books/{book}.txt") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The book '{book}' does not exist. I will print frankenstein instead")
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    
    print(file_contents)

main()
