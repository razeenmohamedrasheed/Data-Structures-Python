class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class singlelist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.ref


L = singlelist()
n = Node(10)
L.head = n
n1 = Node(20)
L.head.ref = n1
n2 =Node(30)
n1.ref = n2
L.display()