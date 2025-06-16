def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lower_text = text.lower()
    character_count = {}
    for char in lower_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(dict):
    return dict['count']

def sort_character_count(character_count):
    split_count_alpha = [{'character': char, 'count': count} for char, count in character_count.items() if char.isalpha()]
    split_count_alpha.sort(key=sort_on, reverse=True)
    return split_count_alpha
