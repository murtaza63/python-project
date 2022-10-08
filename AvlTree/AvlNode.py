from turtle import right


class AVLNode:
    def __init__(self, Element):
        self.value = Element
        self.leftChild = None
        self.rightChild = None
        self.height = 0

        balance_factor = leftHeight - rightHeight 

        leftHeight  = 0 or -1
        rightHeight = 0 or -1 
    
    def __repr__(self):
        return "AVLNode("+repr(self.value)+", balance="+repr(self.height)+", leftChild=" +repr(self.leftChild)+", rightChild="+repr(self.rightChild)+")"
        
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.value, end='\n')
        if self.right:
            self.right.traverseInOrder()

    def traversePreOrder(self):
        print(self.value, end='\n')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end='\n')
    
    


        