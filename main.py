import string

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def main():
    path = "books/frankenstein.txt"
    book = (get_book_text(path)) 
    word_split = book.split()
    word_count = (len(word_split))
    print(f"{word_count} words found in the document")

main()
