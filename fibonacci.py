#Write a Python program to find the sum of the even-valued terms in the Fibonacci series up to a given number. For example, if the input is 100, the program should print: 2 + 8 + 34 = 44.
def fibonacci_sum_even(n):
    fib_sum = 0
    fib_prev = 0
    fib_current = 1

    while fib_current <= n:
        if fib_current % 2 == 0:
            fib_sum += fib_current

        fib_prev, fib_current = fib_current, fib_prev + fib_current

    return fib_sum

# Example usage
limit = 100
result = fibonacci_sum_even(limit)
print("Sum of even-valued terms in Fibonacci series up to", limit, "is:", result)
