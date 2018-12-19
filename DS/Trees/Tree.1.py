
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        
class Tree(object):
    def __init__( self, key,value, leftChild = None, rightChild = None, parent = None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
            
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def hasLeftChild(self):
        return self.leftChild
    
    def hasrightChild(self):
        return self.rightChild

    def isRoot(self):
        return self.parent == None

    def isleaf(self):
        return self.leftChild == None and self.rightChild == None

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeValue(self,key,value,lc,rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasrightChild():
            self.rightChild.parent = self
        



