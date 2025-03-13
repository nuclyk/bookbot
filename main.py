from stats import count_words, count_characters
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")
    characters = count_characters(book)
    print(characters)

main()
