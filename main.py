import string
from stats import get_num_words
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def main():
    path = "books/frankenstein.txt"
    book = (get_book_text(path)) 
    word_count = get_num_words(book)
    print(f"{word_count} words found in the document")

main()
