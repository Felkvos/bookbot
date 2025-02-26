import string
import sys
from stats import get_num_words, character_count, sort_chars
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def main():
    if len(sys.argv) != 2:
        print("usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book = (get_book_text(path)) 
    word_count = get_num_words(book)
    letter_count = character_count(book)
    sorted_chars = sort_chars(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
        
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")

    print("============= END ===============")
                    
    
    
main()
