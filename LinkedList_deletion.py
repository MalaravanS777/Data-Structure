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
        if position<0 and position>=self.listLength():
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
    def deleteValue(self,val):
      if(self.head is None):
        print("List is Empty")
        return
      if(self.head.next==None):
        if(self.head.data==val):
          self.head=None
          return
      currentPosition=0
      currentNode=self.head
      previousNode=currentNode
      while currentNode.data is not val:
        if(currentPosition>=0 and currentPosition<self.listLength()):
          previousNode=currentNode
          currentNode=currentNode.next
          currentPosition+=1
        else:
          print("Value not Present")
      if(currentPosition<self.listLength()):
        previousNode.next=currentNode.next
        currentNode.next=None
    def printList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data,"-->",end="")
            
            currentNode=currentNode.next
        print("None")
linkedList=LinkedList()
firstNode=Node("John")
linkedList.insertEnd(firstNode)
linkedList.printList()
secondNode=Node("Jack")
linkedList.insertHead(secondNode)
linkedList.printList()
thirdNode=Node("Jacob")
linkedList.insertAt(thirdNode,0)
linkedList.printList()
fourthNode=Node("James")
linkedList.insertAt(fourthNode,2)
linkedList.printList()
linkedList.deleteAt(2)
linkedList.printList()
linkedList.deleteHead()
linkedList.printList()
linkedList.deleteEnd()
linkedList.printList()
linkedList.deleteValue("James")
linkedList.printList()
linkedList.deleteValue("Jack")
print("End\n")
linkedList1=LinkedList()
firstNode=Node("Kenma")
linkedList1.insertEnd(firstNode)
linkedList1.printList()
secondNode=Node("Karthi")
linkedList1.insertHead(secondNode)
linkedList1.printList()
thirdNode=Node("Kiran")
linkedList1.insertAt(thirdNode,0)
linkedList1.printList()
fourthNode=Node("Kathir")
linkedList1.insertAt(fourthNode,2)
linkedList1.printList()
linkedList1.deleteAt(2)
linkedList1.printList()
linkedList1.deleteHead()
linkedList1.printList()
linkedList1.deleteEnd()
linkedList1.printList()
linkedList1.deleteValue("Kathir")
linkedList1.printList()
linkedList1.deleteValue("Karthi")
print("End\n")
