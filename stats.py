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

def sort_on(dict_item):
    return list(dict_item.values())[0]

def sort_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        new_dict = {char: count}
        chars_list.append(new_dict)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

