def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    characters = dict()
    for ch in book:
        ch = ch.lower()
        if ch in characters and ch != " ":
            characters[ch] += 1
        else:
            characters[ch] = 1

    return characters

def by_num(dictionary):
    return dictionary["num"]

def convert_dict(characters: dict) -> list:
    char_list = []
    for ch in characters:
       char_list.append({"char": ch, "num": characters[ch]})

    char_list.sort(reverse=True, key=by_num)

    return char_list
