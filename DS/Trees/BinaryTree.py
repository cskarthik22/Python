
'''
[] = List
index 0 = root
index 1 = left
index 2 = right
'''

def BinaryTree(root):
    return [root,[],[]]

def insertLeft(root,ele):
    t = root.pop(1) # left
    if len(t) > 1:
        root.insert(1,[ele,t,[]])
    else:
        root.insert(1,[ele,[],[]])

def insertRight(root,ele):
    t = root.pop(2) # Right child
    if len(t)>1:
        root.insert(2,[ele,[],t])
    else:
        root.insert(2,[ele,[],[]])

def getRootValue(root):
    return root[0]

def setRootValue(root,newval):
    root[0]= newval

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)

insertLeft(r,4)
insertLeft(r,5)
insertRight(r,7)

print(r)
print(getRightChild(r))


   