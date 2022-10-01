


class TreeNode:
   
    def __init__(self, value):
        self.value = value 
        self.children = []
        self.parent = None
    
    def add(self, child):
        child.parent = self
        self.children.append(child)
    
    def forEachDepthFirst(self):
        self.forEachDepthFirst()
        if self.children:
            for child in self.children:
                return child
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add(TreeNode("Mac"))
    laptop.add(TreeNode("Surface"))

    laptop.add(TreeNode("Thinkpad"))


    cellphone = TreeNode("Cell Phone")
    cellphone.add(TreeNode("iPhone"))
    cellphone.add(TreeNode("Google Pixel"))
    cellphone.add(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add(TreeNode("LG"))
    tv.add(TreeNode("Sony"))
    tv.add(TreeNode("CHINA"))
    root.add(laptop)
    root.add(cellphone)
    root.add(tv)
    
    return root



if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
    # print(root.get_level())
    
    pass
    
