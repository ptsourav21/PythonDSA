class Node:
    def __init__(self, value=None):
        self.value= value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head= None
        self.tail = None

SinglylinkedList = SlinkedList()
node1=Node(1)
node2=Node(2)

SinglylinkedList.head=node1
SinglylinkedList.head.next=node2
SinglylinkedList.tail=node2