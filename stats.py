def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    characters = dict()
    for ch in book:
        ch = ch.lower()
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1
    return characters
