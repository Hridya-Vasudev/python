#Swap Two numbers without using a third number.

def swap_numbers(a, b):
    print("Before swapping: a =", a, "b =", b)

    a = a + b
    b = a - b
    a = a - b

    print("After swapping: a =", a, "b =", b)

# Example usage
a = 5
b = 10
swap_numbers(a, b)
