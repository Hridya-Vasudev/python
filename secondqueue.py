# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)
# queue.append(40)
# print(queue)
# queue.pop(0)
# print(queue)

#another way to use queue
# queue=[]
# queue.insert(0,10)
# queue.insert(0,20)
# queue.insert(0,30)
# queue.insert(0,40)
# print(queue)

# #complete q program
# queue=[]
# def enqueue():
#     element=input("Enter the element :")
#     queue.append(element)
#     print(element,"is added")
# def dequeue():
#     if not queue:
#         print("queue is empty")
#     else:
#         e=queue.pop(0)
#         print("removed element is",e)
# def display():
#     print(queue)

# while True:
#     print("select the operation 1.push 2.pop 3.View 4.quit")
#     choice=int(input())
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     elif choice==3:
#         display()
#     elif choice==4:
#         break
#     else:
#         print("Enter the correct option")


#using classes and modules
import collections
q=collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)
q.pop()
print(q)
q.append(50)
q.append(60)
q.append(70)
print(q)
q.popleft()
print(q)

#using priority queue
import queue
q=queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(60)
q.put(30)
q.put(30)#if two values are same then it will be removed using its order.
q.put(40)
print(q)
qu=q.get()
print(qu)
que=q.get()
print(que)
qe=q.get()
print(qe)

