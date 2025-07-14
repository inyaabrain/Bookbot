def word_count(book_text):
    count = 0
    total_words = book_text.split()
    for words in total_words:
        count += 1
    return count

def character_count(book_text):
    book_text = book_text.lower()
    characters = {}
    for character in book_text:
        characters[character] = characters.get(character, 0) + 1
    return characters

def sort_key(characters):
     return characters["num"]

def sort_char(character_count):
    character_list = [{"char": key, "num": value} for key, value in character_count.items() if key.isalpha()]
    character_list.sort(reverse=True, key=sort_key)
    return character_list
