def get_word_count(book_content):
    word_count = 0
    for word in book_content.split():
        word_count += 1
    return word_count

def count_characters(book_content):
    chars = { }

    for char in book_content:
        lower_char = char.lower()
        if lower_char in chars:
            chars[lower_char] += 1
        else:
            chars[lower_char] = 1

    return chars

def sort_on(dict):
    return dict["count"]

def sort_chars_by_count(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list