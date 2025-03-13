from stats import convert_dict, count_words, count_characters
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    characters = count_characters(book)
    characters = convert_dict(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")

    for ch in characters:
        if ch["char"].isalpha():
            print(f'{ch["char"]}: {ch["num"]}')
    print("============= END ===============")


main()
