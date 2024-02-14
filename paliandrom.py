# Write a Python program to find all palindrome numbers between two given numbers. For example, if the input is 100 and 200, the program should print all palindrome numbers between 100 and 200, such as 101, 111, 121, and so on.
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_palindrome_numbers(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes

# Example usage
start_num = 100
end_num = 200
palindrome_nums = find_palindrome_numbers(start_num, end_num)
print("Palindrome numbers between", start_num, "and", end_num, "are:")
for num in palindrome_nums:
    print(num)
