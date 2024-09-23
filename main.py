from bookcount import count_words, char_count, display_report

def read():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def main():
    file = read()
    word_count = count_words(file)
    character_count = char_count(file)
    display_report(file)

if __name__ == "__main__":
    main()