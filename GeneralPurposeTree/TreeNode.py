


class TreeNode:
    children = [TreeNode] = []
    def __init__(self, value):
        self.value = value 
    
    def add(self, child: TreeNode):
        self.children.append(child)
    
