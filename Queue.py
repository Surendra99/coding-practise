from Node import Node
class Queue:
    head=None

    @classmethod
    def enqueue(self,data):
        if(self.head==None):
            self.head = Node(data)
            return
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = Node(data)
        return temp

    @classmethod
    def dequeue(self):
        temp = self.head
        self.head = self.head.next
        return temp
