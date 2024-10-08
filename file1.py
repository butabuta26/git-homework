def letters_unique(input_string):
    input_string = input_string.lower()
    unique_letters = set()
    
    for char in input_string:
        if char.isalpha():
            if char in unique_letters:
                return False
            unique_letters.add(char)
    return True

print(letters_unique("Guten Tag"))
print(letters_unique("11"))
print(letters_unique("adolf"))