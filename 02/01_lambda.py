'''
Note: Body of lamda should be single statement

'''

def add(x,y):
    return x+y;

print(add(2,3))

l_add = lambda x,y: x+y
print(l_add(2,3))

def rev(str):
    return str[::-1]

print(rev('python'))

l_rev = lambda str: str[::-1]
print(l_rev('python'))
