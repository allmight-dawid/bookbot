import sys
from stats import word_count, character_count, sort_list

def main():
    filepath = 0
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    txt_contents = get_book_text(filepath)
    word_count(txt_contents)
    char_dictionary = character_count(txt_contents)
    sort_list(char_dictionary)
    dictionary_print(char_dictionary)

def dictionary_print(sorted_list):
    for char, count in sorted_list.items():
        if char .isalpha():
            print(f"{char}: {count}")
        else:
            pass

def get_book_text (filepath):
    with open (filepath) as f:
        txt_contents = f.read()
    return txt_contents

main()