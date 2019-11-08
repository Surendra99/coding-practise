from Node import Node
class Queue:
    def __init__(self):
        self.head=None

    def enqueue(self,data):
        if(self.head==None):
            self.head = Node(data)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)
        return temp

    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        return temp

    def length(self):
        temp = self.head
        count=0
        while temp !=None:
            temp = temp.next
            count+=1
        return count
    def print(self):
        temp = self.head;        
        while temp !=None:
            print(temp.data.data,end=",")
            temp = temp.next
