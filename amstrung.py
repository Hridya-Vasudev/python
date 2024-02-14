#Write a Python program to find the smallest Armstrong number with n digits. For example, if n is 3, the program should find the smallest 3-digit Armstrong number.
def is_armstrong_number(num):
    num_str = str(num)
    n = len(num_str)
    sum_of_powers = sum(int(digit) ** n for digit in num_str)
    return num == sum_of_powers

def find_smallest_armstrong(n):
    start = 10 ** (n - 1)
    end = 10 ** n - 1
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            return num

# Example usage
n = 3
smallest = find_smallest_armstrong(n)
print("The smallest", n, "-digit Armstrong number is:", smallest)
