#1. Write a Python program to Count all letters, digits, and special symbols from the given 

#string Input = “P@#yn26at^&i5ve”

def count_chars(string):
    chars = digits = symbols = 0
    for ch in string:
        if ch.isalpha():
            chars += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1
    return chars, digits, symbols

input_str = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars(input_str)
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")
#output
#Chars = 8 Digits = 3 Symbol = 4
