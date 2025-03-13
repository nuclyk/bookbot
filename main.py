from stats import convert_dict, count_words, count_characters
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = None
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])

    characters = count_characters(book)
    characters = convert_dict(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")

    print("--------- Character Count -------")
    for ch in characters:
        if ch["char"].isalpha():
            print(f'{ch["char"]}: {ch["num"]}')
    print("============= END ===============")


main()
