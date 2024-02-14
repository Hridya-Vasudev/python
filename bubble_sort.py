def bubble_sort(elements):
    size=len(elements)
    for k in range(size-1):
     for i in range(size-1-k):
        if elements[i] > elements[i+1]:
            tmp=elements[i]
            elements[i]=elements[i+1]
            elements[i+1]=tmp




elements=[5,9,2,1,34,12,32,10,56,7,85]
bubble_sort(elements)
print(elements)

#in the second for loop we can ignore the last two elemets bcz it is already sorted, so that we are using the size-1-k