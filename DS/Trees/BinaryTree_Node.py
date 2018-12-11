
class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        t = BinaryTree(newNode)
        if self.leftChild == None:
            self.leftChild = t
        else:
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        t = BinaryTree(newNode)  
        if self.rightChild == None:
            self.rightChild = t     
        else:
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key

    def printLeftTree(self):
       res = []
       root = self
       while root.leftChild:
           root = root.leftChild
           res = res + [root.key] 
       return res

    def printRightTree(self):
       res = []
       root = self
       while root.rightChild:
           root = root.rightChild
           res = res + [root.key] 
       return res
    
    def printTree(self):
        root = [self.key]

        print(root + [self.leftChild.printLeftTree()] + [ self.rightChild.printRightTree() ])

            


n  = BinaryTree(3)

n.insertLeft(4)

n.insertLeft(6)
n.insertLeft(7)
n.insertRight(5)
#print(n.key)
#print(n.getLeftChild())
#print(n.getRightChild().getRootVal())
#print(n.getRootVal())
#n.printLeftTree()
#n.printRightTree()
n.printTree()

#n.printTree()
