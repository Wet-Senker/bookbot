def get_num_words(text: str) -> None:
    words = text.split()
    print(f"Found {len(words)} total words")

def get_character_count(text: str):
    dict_characters = {}
    for char in text.lower():
        dict_characters.setdefault(char, 0)
        dict_characters[char] += 1
    return dict_characters
 
def get_sorted(my_dict: dict):
    sorted_dict = dict(sorted(my_dict.items()))
    return sorted_dict