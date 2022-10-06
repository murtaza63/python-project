class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
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
        else:
            print(None)
        if self.right:
            self.right.traversePreOrder()
        else:
            print( None)
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end='\n')
    
    

    def diagram(self, top:str, root:str,bottom:str) -> str:
        
        if self.value:
            return self.value
        else:
            return root + "None\n"

        if self.left == None and self.right == None:
            return root + self.value,"\n"
        return diagram(self.right, top, " ", top, "┌──", top, "| ")
        + root + self.value,"\n"
        + diagram(self.left, bottom, "| ", bottom, "└──", bottom, " " )
        

    


    def printTree(self):
        return self.value
