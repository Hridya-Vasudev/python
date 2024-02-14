def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  


my_list = [4, 2, 7, 1, 9, 5]
element_to_find = 2

result = linear_search(my_list, element_to_find)

if result != -1:
    print(f"Element {element_to_find} found at index: {result}")
else:
    print(f"Element {element_to_find} not found in the list")
