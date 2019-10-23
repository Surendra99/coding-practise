from Node import Node
from BinaryTreeNode import BinaryTreeNode
from Queue import Queue
import collections

def top_view(root):
    level_dict = {}
    level_dict[0] = root.data
    queue = Queue()
    queue.enqueue({'value':root,'level':0})
    while(queue.head != None):
        node = queue.head.data['value']
        level = queue.head.data['level']
        if level not in level_dict:
            level_dict[level] = node.data
        if node.left is not None:
            queue.enqueue({'value':node.left,'level':level-1})    
        if node.right is not None:
            queue.enqueue({'value':node.right,'level':level+1})
        queue.dequeue()    
    print(level_dict)

root  = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)

root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)

root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
# top_view(root)

root1  = BinaryTreeNode(1)
root1.left = BinaryTreeNode(2)
root1.right = BinaryTreeNode(3)

root1.left.right = BinaryTreeNode(4)
root1.left.right.right = BinaryTreeNode(5)
root1.left.right.right.right = BinaryTreeNode(6)
top_view(root1)