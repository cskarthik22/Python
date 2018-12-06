'''
Stack: Last In First Out ( LIFO )
push(), pop(), peek(), isEmpty(), size()

'''

class Stack(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def peek(self):
        #return self.items[len(self.items)-1]
        return self.items[~0]

s = Stack()
s.push('one')
s.push(2)
s.push(True)

print(s.isEmpty(), s.size(), s.peek())
s.pop()
s.pop()
print(s.isEmpty(), s.size(), s.peek())
s.pop()
print(s.isEmpty(), s.size())

