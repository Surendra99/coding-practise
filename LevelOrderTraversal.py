from BinaryTreeNode import BinaryTreeNode
from Queue import Queue

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

queue = Queue()
queue.enqueue(root)
while(queue.head != None):
    binaryNode = queue.head.data
    print(binaryNode.data)
    if binaryNode.left is not None:
        queue.enqueue(binaryNode.left)
    if binaryNode.right is not None:
        queue.enqueue(binaryNode.right)
    queue.dequeue()
