#If an array is a=[1,2,4,32,12,6,8] and b=[2,6,10,12,14,17] print or return the numbers present in a not in b
def find_missing_numbers(a, b):
    missing_numbers = []
    for num in a:
        if num not in b:
            missing_numbers.append(num)
    return missing_numbers

# Example usage
a = [1, 2, 4, 32, 12, 6, 8]
b = [2, 6, 10, 12, 14, 17]
missing = find_missing_numbers(a, b)
print("Numbers present in a but not in b:", missing)
