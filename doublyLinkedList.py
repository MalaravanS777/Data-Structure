class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def listLength(self):
        length=0
        currentNode=self.head
        while currentNode is not None:
            length+=1
            currentNode=currentNode.next
        return length
    def insertHead(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            tempNode=self.head
            self.head=newNode
            self.head.next=tempNode
            tempNode.previous=self.head
            del tempNode
    def insertEnd(self,newNode):
        if self.head is None:
            self.insertHead(newNode)
            return
        else:
            lastNode=self.head
            while lastNode.next is not None:
                lastNode=lastNode.next
            lastNode.next=newNode
            newNode.previous=lastNode
    def insertAt(self,newNode,position):
        if(position==0):
            self.inserHead(newNode)
            return
        if (position<0 and position>=self.listLength()):
            print("Invalid Position")
            return
        currentPosition=0
        previousNode=self.head
        currentNode=self.head
        while True:
            if(currentPosition==position):
                newNode.next=previousNode.next
                previousNode.next=newNode
                newNode.previous=previousNode
                currentNode.previous=newNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition+=1
    def deleteHead(self):
        tempNode=self.head
        self.head=tempNode.next
        self.head.previous=None
        tempNode.next=None
        del tempNode
    def deleteEnd(self):
        currentNode=self.head
        previousNode=self.head
        while currentNode.next is not None:
            previousNode=currentNode
            currentNode=currentNode.next
        previousNode.next=None
        currentNode.previous=None
    def deleteAt(self,position):
        currentPosition=0
        currentNode=self.head
        previousNode=self.head
        nextNode=self.head
        while True:
            if(currentPosition==position):
                previousNode.next=currentNode.next
                nextNode.previous=currentNode.previous
                break
            previousNode=currentNode
            currentNode=currentNode.next
            nextNode=currentNode.next
            currentPosition+=1
                
    def printList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data,"-->",end="")
            currentNode=currentNode.next
        print(None)
    def printIndex(self,position):
        if(position<0 or position>=self.listLength()):
            print("Invalid Position")
            return
        currentPosition=0
        currentNode=self.head
        while True:
            if(currentPosition==position):
                print(currentNode.data)
                break
            currentPosition+=1
            currentNode=currentNode.next
doublyLinkedList=DoublyLinkedList()
firstNode=Node("Jack")
doublyLinkedList.insertHead(firstNode)
secondNode=Node("James")
doublyLinkedList.insertHead(secondNode)
thirdNode=Node("John")
doublyLinkedList.insertEnd(thirdNode)
fourthNode=Node("Janda")
doublyLinkedList.insertAt(fourthNode,1)
fifthNode=Node("Jan")
doublyLinkedList.insertEnd(fifthNode)
doublyLinkedList.printList()
doublyLinkedList.deleteHead()
doublyLinkedList.printList()
doublyLinkedList.deleteEnd()
doublyLinkedList.printList()
doublyLinkedList.deleteAt(1)
doublyLinkedList.printList()
doublyLinkedList.printIndex(1)
