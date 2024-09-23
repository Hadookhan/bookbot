

def count_words(book):
    book_word_list = book.split()
    count = 0
    for _ in range(len(book_word_list)):
        count += 1
    
    return count

def char_count(book):
    book_word_list = book.lower().split()
    char_dict = {}
    for word in book_word_list:
        char_list = list(word)
        for char in char_list:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def display_report(book):
    get_character_dict = char_count(book)
    get_word_count = count_words(book)
    print(f"--- Begin report of books/frankenstein.txt ---\n{get_word_count} words found in the document")

    for key, value in get_character_dict.items():
        print(f"The {key} character was found {value} times")
        