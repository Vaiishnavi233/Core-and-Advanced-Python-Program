#2. Write a Python program to remove duplicate characters of a given string. 
#Input = “String and String Function” 

def remove_duplicate_words(sentence):
    words = sentence.split()
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

input_str = "String and String Function"
output_str = remove_duplicate_words(input_str)
print(output_str)
#Output
#String and Function
