
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next
    
    def reverse(self):
        temp = self.tail
        while temp:
            print temp.data
            temp = temp.prev

        
if __name__ == "__main__":
    dll = DoubleLinkedList()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    dll.head = a
    a.next = b
    a.prev = None
    b.next = c
    b.prev = a
    c.next = dll.tail
    c.prev = b

    dll.reverse()