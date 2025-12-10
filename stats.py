def word_count (txt_contents):
    text_list = txt_contents.split()
    count = len(text_list)
    return print(f"Found {count} total words")

def character_count(txt_contents):
    char_count = {}
    lowercase_text = txt_contents.lower()
    for char in lowercase_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_list(char_count):
    sorted_list= []
    for char, count in char_count.items():
        small_dict = {}
        small_dict["char"] = char
        small_dict["num"] = count
        sorted_list.append(small_dict)
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list