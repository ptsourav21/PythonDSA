class Node:
    def __init__(self, value=None):
        self.value= value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head= None
        self.tail = None

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node=node.next
            
    def insertSLL(self, value, location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location ==0:
                newNode.next=self.head
                self.head=newNode
            elif location ==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next = newNode
                newNode.next=nextNode
    def traverseSLL(self):
        node=self.head
        if node is None:
            print("Single Linked List is Null")
        else:
            while node is not None:
                print(node.value)
                node=node.next

    def searchLinkedList(self, nodeValue):
        if self.head is None:
            return "The List is Empty"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    return node.value
            return "Value is not in the list"

    def deleteNode(self, location):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head= None
                    self.tail= None
                else:
                    self.head=self.head.next
            elif location==1:
                if self.head==self.tail:
                    self.head= None
                    self.tail= None
                else:
                    node = self.head
                    while node:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                nextNode=node.next
                node.next=nextNode.next
                