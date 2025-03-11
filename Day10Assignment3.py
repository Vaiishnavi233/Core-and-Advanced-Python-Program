#3. Write a Python program to find duplicate values from a list and display those.
def find_duplicates(lst):
    duplicates = []
    seen = set()
    
    for num in lst:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates

# Example usage
numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
print("Duplicates:", find_duplicates(numbers))
#output
#Duplicates: [2, 3, 1]
