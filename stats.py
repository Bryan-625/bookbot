def num_words(text):
    text_split = text.split()
    return len(text_split)

def count_characters(text):
    char_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dict):
    dict_tuple = dict.items()
    sorted_dict = []
    for key, value in dict_tuple:
        if key.isalpha():
            sorted_dict.append({"char": key, "num": value})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict