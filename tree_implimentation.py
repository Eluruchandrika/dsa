class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

if __name__=='__main__':
    root=node(1)
    root.left=node(2)
    root.right=node(2) 
    root.left.left=node(3)
    root.left.right=node(4)
