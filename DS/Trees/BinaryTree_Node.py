
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

n  = BinaryTree(3)
t = n
t.insertLeft(4)
t.insertLeft(6)
t.insertLeft(7)
t.insertRight(5)
print(n.getLeftChild().getRootVal())
print(n.getRightChild().getRootVal())
print(n.getRootVal())

