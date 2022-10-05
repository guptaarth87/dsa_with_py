class TreeNode():
     def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
     def addChild(self,child):
        child.parent=self
        self.children.append(child)

     def printing(self):
         temp=self.children
         while not temp.empty():
            print()

def build_tree():
    root=TreeNode('Languages')

    python=TreeNode('Python')
    javascript=TreeNode('JavaScript')
    java=TreeNode('java')

    root.addChild(python)
    root.addChild(javascript)
    root.addChild(java)



if __name__ == "__main__":
    build_tree()