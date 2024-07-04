class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def listLength(self):
        length=0
        currentNode=self.head
        while currentNode is not None:
            length+=1
        return length
    def insertHead(self,newNode):
        tempNode=self.head
        self.head=newNode
        newNode.next=tempNode
    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    lastNode.next=newNode
                    break
                lastNode=lastNode.next
    def insertAt(self,newNode,position):
        if position==0:
            self.insertHead(newNode)
            return
        if position==-1:
            self.insertEnd(newNode)
            return
        if position<0 and position>_self.listLength():
            print("Invalid Position")
        currentPosition=0
        currentNode=self.head
        while True:
            if currentPosition == position-1:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            currentPosition+=1
            previousNode=currentNode
            currentNode=currentNode.next
    def deleteHead(self):
        previousHead=self.head
        self.head=previousHead.next
        previousHead.next=None
    def deleteEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next=None
    def deleteAt(self,position):
        if position<0 and position>=self.listLength():
            print("Invalid Position")
            return
        if position==0:
            self.deleteHead()
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                previousNode.next=currentNode.next
                currentNode.next=None
                break
            previousNode=currentNode
            currentPosition+=1
            currentNode=currentNode.next
    def printList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data,"-->",end="")
            
            currentNode=currentNode.next
        print("None")
linkedList=LinkedList()
firstNode=Node("John")
linkedList.insertEnd(firstNode)
secondNode=Node("Jack")
linkedList.insertHead(secondNode)
thirdNode=Node("Jacob")
linkedList.insertAt(thirdNode,0)
fourthNode=Node("James")
linkedList.insertAt(fourthNode,2)
linkedList.deleteAt(2)
linkedList.deleteHead()
linkedList.deleteEnd()
linkedList.printList()