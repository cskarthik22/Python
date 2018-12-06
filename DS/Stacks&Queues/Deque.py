'''
Same as queue, but the only difference is we can add/remove items at either end.

---------------------------------
Back | 0 |  1 |  2 |  3 | 4  | Front
----------------------------------
addrear() at index 0              addFront() at the end
removeRear() at index 0           removefront() at the end

'''

class Deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)    

d = Deque()
d.addFront('Hello')
d.addRear('World')

print(d.size(), d.isEmpty())
print(d.removeFront() + ' ' + d.removeRear())
print(d.size(), d.isEmpty())