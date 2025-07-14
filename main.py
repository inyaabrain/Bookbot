import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]

def get_book_text(text):
    with open(text) as f:
        text = f.read()
    return text


def main():
    from stats import word_count
    from stats import character_count
    from stats import sort_char
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    num_characters = character_count(book_text)
    character_list = sort_char(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in character_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
