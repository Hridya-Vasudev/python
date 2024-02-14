def insertion_sort(A):
    for i in range(1,len(A)):
        anchor=A[i]
        j=i-1
        while j >= 0 and anchor < A[j]:
            A[j+1]=A[j]
            j=j-1
        A[j+1]=anchor

A=[11,9,29,7,2,15,28]
insertion_sort(A)
print(A)

test=[
    [11,9,29,7,2,15,28],
    [2,30,1,10],
    [],
    [3]

]
for elements in test:
    insertion_sort(elements)
    print(elements)




#exeresice 1 find the median of a given list[2,1,5,7,2,0,5]

list1 = [2, 1, 5, 7, 2, 0, 5]
length = len(list1)

def insertion_sort(list1):
    for i in range(1, length):
        key = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > key:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = key

def find_median(list1):
    median = 0
    if length % 2 == 0:
        median = (list1[length // 2] + list1[length // 2 - 1]) / 2
    else:
        median = list1[length // 2]
    return median


insertion_sort(list1)
for i in range(len(list1)):
    print(list1[i - 1], end=" ")

median = find_median(list1)

if length % 2 == 0:
    median = median / 2
    print(median, end=" ")
else:
    print(median, end=" ")
    for i in range(1, 4):
        print(median + i * 0.5, end=" ")




       
            