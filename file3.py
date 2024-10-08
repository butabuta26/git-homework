def reverser(s):
    left = 0                 
    right = len(s) - 1      
    reversed_str = ""

    while left <= right:
        reversed_str += s[right]
        right -= 1
    return reversed_str

print(reverser("holaaa"))
print(reverser("einferstanden"))