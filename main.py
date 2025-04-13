from stats import get_num_words, get_character_count, get_sorted
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    get_num_words(text)
    character_dict = get_character_count(text)
    sorted_dict = get_sorted(character_dict)

    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()