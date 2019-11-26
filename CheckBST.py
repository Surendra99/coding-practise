from BinaryTreeNode import BinaryTreeNode
class CheckBST:
    root = BinaryTreeNode(3)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(5)

    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(4)
    min,max=None

    def validateBst(self,node,min,max):
        if node == None:
            return True
        if min == None and max == None:
            min,max = node.data
        valid = False    
        if node.left != None and node.left.data > min:
            return False
        else:
            valid = validateBst(node.left,node.left.data)    