
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def display(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next


if __name__ == '__main__':
    sll = SingleLinkedList()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    sll.head = a
    a.next = b
    b.next = c
    c.next = sll.tail
    sll.display()
    




