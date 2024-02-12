class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class linkedlist:
    def __init__(self):
        self.head = None

    def displayList(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.ref


l = linkedlist()
n = Node(10)
l.head = n
n1 = Node(20)
l.head.ref = n1
n2 = Node(30)
n1.ref = n2
l.displayList()
