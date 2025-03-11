# 2. Write a Python program to get the largest and smallest number from a list without built in functions.
def find_min_max(lst):
    smallest = lst[0]
    largest = lst[0]
    
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
            
    return smallest, largest

# Example usage
numbers = [3, 1, 7, 9, 2, 8]
smallest, largest = find_min_max(numbers)
print("Smallest:", smallest)
print("Largest:", largest)
#
