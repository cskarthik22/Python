'''
Queue - First In First Out ( FIFO )
enqueue(), dequeue(), isEmpty(), size()

Add from Back & remove from Front

---------------------------------
Back | 0 |  1 |  2 |  3 | 4  | Front
----------------------------------
Enqueue() at index 0              Dequeue() at the end
          
'''

class Queue(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

q = Queue()

q.enqueue('one')
q.enqueue(2)
q.enqueue(True)

print(q.dequeue(),q.size(), q.isEmpty())
print(q.dequeue(),q.size(), q.isEmpty())
print(q.dequeue(),q.size(), q.isEmpty())
