from Node import Node
class Stack:
    head = None

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
           node = Node(data)
           node.next = self.head
           self.head = node

    def peek(self):
        if self.head == None:
            return -1
        return self.head.data

    def isEmpty(self):
        return self.head == None    

    def pop (self):
        node = self.head
        self.head = self.head.next
        return node.data

    def print(self):
        node = self.head
        if self.head == None:
            print('EOD')
            return
        while node is not None:
                print(node.data)
                node = node.next
