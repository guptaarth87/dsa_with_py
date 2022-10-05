class TreeNode():
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
    
    def printing(self):
        temp=self
        while temp.val:
            print("data : ",temp.val)
            if temp.left and temp.right:
                print("left : {}, right: {}".format(temp.left.val,temp.right.val))
            elif temp.left:
                print("left: {}".format(temp.left.val))
            elif temp.right:
                print("left: {}".format(temp.left.val))
            if temp.left:
               temp=temp.left
            else:
                break
    
if __name__ == "__main__":
    root = TreeNode(1)
    ''' following is the tree after above statement
        1
      /   \
     None  None'''
    root.left=TreeNode(2)
    root.right=TreeNode(3)

    ''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
    None None None None'''
    root.right.left=TreeNode(7)
    root.right.right=TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # For root, l = 0, number of nodes = 20 = 1 l=level

    root.printing()
