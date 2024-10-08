def count_letters(input_string):
    letter_count = {}
    
    for char in input_string.lower():
            if char.isalpha():
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1
    return letter_count

print(count_letters("Hello"))