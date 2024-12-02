def main():
    book_path = "books/frankenstein.txt"
    text = read_book_contents(book_path)
    num_words = count_letters(text)
    chars_dict = letter_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch , "num": num_chars_dict[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

    
def letter_dict(text):
    letters = {}
    for c in text:
        lowered = c.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

    
def count_letters(text):
    letters = text.split()
    return len(letters)
    
    
def read_book_contents(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

main()