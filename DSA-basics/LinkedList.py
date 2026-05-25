class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self,head=None):
        self.head=head

#adding linked list elements
    def add(self,data):
        new=Node(data)
        if(self.head):
            temp=self.head            #1
            while(temp.next!=None):   #3
                temp=temp.next
            temp.next=new             #2
            # print(temp.next)
        else:
            self.head=new
        # print(new.data)

#printing linked list
    def printList(self):
        current=self.head
        while(current):
            print(current.data)
            current=current.next
#insert value in the beginning
    def insert(self,data):
        new=Node(data)
        temp=self.head
        new.next=self.head
        # print(new.next)
        self.head=new
        # print(self.head.data)
#insert at the end
    def insertEnd(self,data):
        new=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new

        
#insert after a given node

L1=LinkedList()
L1.add(14)
L1.add(15)
L1.add(16)
L1.add(17)
L1.add(18)
L1.insert(13)
L1.insertEnd(19)
L1.printList()


        