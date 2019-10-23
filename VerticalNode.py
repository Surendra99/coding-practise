import Node


class VerticalNode(Node.Node):
    level = 0
    def __init__(self,data,level):
        self.level = level
        self.data = data    
