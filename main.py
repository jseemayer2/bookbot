def read_book():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def count_words(book: str):
    nb_words = len(book.split())
    return nb_words

def count_characters(book: str):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    nb_char = {}
    for letter in alphabet:
        nb_char[letter] = book.lower().count(letter)
    return nb_char

def main():
    book = read_book()
    nb_words = count_words(book)
    nb_char = count_characters(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{nb_words} words found in the document\n")
    for k,v in nb_char.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")
    return

main()