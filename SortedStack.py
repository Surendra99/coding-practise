from Stack import Stack

primaryStack = Stack()
secondaryStack = Stack()

def push(data):
    while not primaryStack.isEmpty():
        if primaryStack.peek() >= data:
            break
        secondaryStack.push(primaryStack.pop())
    primaryStack.push(data)
    while not secondaryStack.isEmpty():
        primaryStack.push(secondaryStack.pop())

push(5)
push(3)
push(4)
push(1)
push(2)
primaryStack.print()