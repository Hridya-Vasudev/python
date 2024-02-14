def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge(left)
    right=merge(right)
    return merge_sort(left,right)

def merge_sort(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i = j= 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i < len_a:
        sorted_list.append(a[i])
        i+=1
    while j < len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list
if __name__=='__main__':
   arr=[10,34,12,49,56,100,21,9,32,67,101]
   print(merge(arr))

   #the above problem will take up space, for the convenient program, we need to free up the space. so we need to remove the new array.

   def merge(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge(left)
    merge(right)
    return merge_sort(left,right,arr)

def merge_sort(a,b,arr):
    
    len_a=len(a)
    len_b=len(b)
    i = j= k= 0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
           arr[k]=a[i]
           i+=1
             
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i < len_a:
       arr[k]=a[i]
       i+=1
       k+=1
    while j < len_b:
        arr[k]=b[j]
        j+=1
        k+=1
    return arr
if __name__=='__main__':
   arr=[10,34,12,49,56,100,21,9,32,67,101]
   print(merge(arr))
#this is the most efficient method.


#exresice: Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

# elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]
# merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

# merge_sort(elements, key='age', descending=True)
# This will sort elements by time_hours and your sorted list will look like,

# elements = [
#         {'name': 'rajab', 'age': 12, 'time_hours': 3},
#         {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#         {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#         {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#     ]
# But if you call it like this,

# merge_sort(elements, key='name')
# output will be,

# elements = [
#         { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#     ]

def merge_sort(arr, key, descending=True):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge(arr, left, right, key, descending)


def merge(arr, left, right, key, descending):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if (not descending and left[i][key] <= right[j][key]) or (descending and left[i][key] >= right[j][key]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]

    merge_sort(elements, key='time_hours', descending=False)
    print(elements)
