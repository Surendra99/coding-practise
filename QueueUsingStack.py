from Stack import Stack

stackNewest = Stack()
stackOldest = Stack()

def shitShacks():
    while not stackNewest.isEmpty():
        stackOldest.push(stackNewest.pop())

def push(data):
    stackNewest.push(data)

def pop():
    if stackOldest.isEmpty:
        shitShacks()
    stackOldest.pop()    

push(2)
push(3)
pop()
stackOldest.print()