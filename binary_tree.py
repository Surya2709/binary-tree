class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def get_data(self):
        return self.data

class BinaryTree:
    def __init__(self):
        self.root=None
        #End Init
    def InsertNode(self,data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._InsertNode(data,self.root)
        #End
    def _InsertNode(self,data,node):
        if(data < node.data):
            if(node.left != None):
                self._InsertNode(data,node.left)
            else:
                node.left=Node(data)
        else:
            if(node.right != None):
                self._InsertNode(data,node.right)
            else:
                node.right=Node(data)
        #End
    def DeleteBinaryTree(self):
        self.root=None
        #End
    def Isempty(self):
        return self.root==None
        #End
    def PrintTree(self):
        if self.root != None:
            self._PrintTree(self.root)

    def _PrintTree(self,node):
        if(node != None):
            self._PrintTree(node.left)
            print(str(node.data)+ ' ')
            self._PrintTree(node.right)
            print(str(node.data)+' ')
        #End

    def find(self,data):
        if(self.root != None):
            return self._find(data,self.root)
        else:
            return None
        #End

    def _find(self,data,node):
        if (data == node.data):
            return node
        elif(data < node.data and node.left != None):
            self._find(data,node.left)
        elif(data > node.data and node.right != None):
            self._find(data,node.right)
        #End

#Driver Code
if __name__ == "__main__":
    b=BinaryTree()
    b.InsertNode(17)
    b.InsertNode(1)
    b.InsertNode(13)
    b.InsertNode(6)
    b.InsertNode(9)
    b.InsertNode(7)
    b.InsertNode(76)
    b.InsertNode(32)
    b.InsertNode(21)
    b.InsertNode(25)
    b.PrintTree()
    b.find(7)
    b.InsertNode(34)
    b.PrintTree()
    
    


    