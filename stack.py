print("Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.")
#for push operation:-we need to remove some words 'data' 'follows' 'particular', first we need to remove 'data' so the data will pushed to stack first. 
#when we press the cntrl+z the last removed item will be appeared first. so the elements from the stack removed using pop() operation.
#the application for the stack is when we are using the reverse of the string and used in expression evaluation 
#when we are implimenting stack using list the two operations will be push-->append pop-->pop

stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
stack.pop()
print(stack)
len(stack)==0 or not stack #using to check the stack is empty or not

#a complete application impliment stack using list

stack=[]
def push():
    element=input("Enter the element :")
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element is",e)
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct option")
    


#in another way

stack=[]
def push():
    if len(stack)==n:
        print("stack is full")
    else:
        element=input("Enter the element :")
        stack.append(element)
        print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element is",e)
n=int(input("limit of stack:"))
while True:
    print("select the operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct option")


#stack using different modules
# first module is collection module  there is a class called deque, deque means double ended queue 
import collections
stack=collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
#second the queue module there is a class called lifoqueue here push-->put pop-->get

import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(30)
stack.put(40)
stack_list=list(stack.queue)
print(stack_list)
stack.get()
stack_list1=list(stack.queue)
print(stack_list1)

#setting limit
import queue as stdlib_queue

stack=queue.LifoQueue(3)
stack.put(10)
stack.put(30)
stack.put(40)
stack.put(50,timeout=1)
stack_list=list(stack.queue)
stack.get()
stack_list1=list(stack.queue)
print(stack_list1)



