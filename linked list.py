#Single linked list
#we can add in the begining , in between and the end
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
#node1=Node(10)
class LinkedList():
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
LL1=LinkedList()
LL1.print_LL()




