def get_num_words(text):
    word_split = text.split()
    word_count = (len(word_split))
    return word_count
def character_count(letters):
    char_counts = {}
    lower_c = letters.lower()
    for char in lower_c:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
            


