#If an array=[1,2,3,32,45,6] find the biggest number and the smallest number.
def find_max_min(arr):
    if len(arr) == 0:
        return None, None

    maximum = minimum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum

# Example usage
array = [1, 2, 3, 32, 45, 6]
max_num, min_num = find_max_min(array)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
