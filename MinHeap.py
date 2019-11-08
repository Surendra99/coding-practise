from BinaryTreeNode import BinaryTreeNode
from Queue import Queue

def buildTree(element,queue):
    head = queue.head
    node = BinaryTreeNode(element)
    if head.data.left == None:
        head.data.left = node
        queue.enqueue(node)
    elif head.data.right == None:
        head.data.right = node
        queue.enqueue(node)
        queue.dequeue()

def heapTree(node):
    if node == None:
        return    
    if node.left == None and node.right == None:
        return
    heapTree(node.left)
    heapTree(node.right)
    heapify(node)

def heapify(node):
    if node.left != None and node.left.data < node.data:
        temp = node.data
        node.data = node.left.data
        node.left.data = temp
    if node.left != None and node.right.data < node.data:
        temp = node.data
        node.data = node.right.data
        node.right.data = temp    
        


queue = Queue()
array = [5,2,3,4,1]        
node = BinaryTreeNode(array[0])     
queue.enqueue(node)
for i in range(1,len(array)):
    buildTree(array[i],queue)
node.levelorder(node)   