def split_letters(string):
    letters = []
    for char in string:
        letters.append(char)
    return letters

# Test case
word = input("")
letter_list = split_letters(word)
print(letter_list)