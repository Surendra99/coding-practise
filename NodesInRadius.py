from BinaryTreeNode import BinaryTreeNode

# {height,sideToRoot}
def findNode(node,level,value,helperMap):
    if node == None:
        return False
    if node.data == value:
        helperMap['height'] = level
        return True
    result = findNode(node.left,level+1,value,helperMap)
    if result == True:
        node.data = {'data':node.data,'side':'left'}
        # print(node.data)        
        return True
    result = findNode(node.right,level+1,value,helperMap)
    if result == True:
        node.data = {'data':node.data,'side':'right'}
        # print(node.data)        
        return True
    

def printElementsWithInRadius(node,distance,radius,givenValue):
    if node == None:
        return
    if distance > radius and isinstance(node.data,(int)):
        return 
    if distance == radius:
        print(node.data)
    if isinstance(node.data,(int)):  
        leftDistance, rightDistance = (1,1) if node.data == givenValue else (distance+1,distance+1)
    else:
        leftDistance, rightDistance = (distance-1,distance+1) if node.data['side'] == 'left' else (distance+1,distance-1)
    printElementsWithInRadius(node.left,leftDistance,radius,givenValue)
    printElementsWithInRadius(node.right,rightDistance,radius,givenValue)

def printRadius(root,value,radius): 
    helperMap = {'height':-1}
    findNode(root,0,value,helperMap)
    if helperMap['height'] == -1:
        print('Given Element not Found')
    printElementsWithInRadius(root,helperMap['height'],radius,value)  

def set1():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    root.left.left.left = BinaryTreeNode(14)
    root.left.left.right = BinaryTreeNode(12)
    
    root.left.left.left.left = BinaryTreeNode(15)
    root.left.left.left.right = BinaryTreeNode(18)

    printRadius(root,7,3)
set1()    
