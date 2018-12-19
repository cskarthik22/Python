
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertFirst(self, data):
        self.head = Node(data,self.head)
    
    def size(self):
        count =0
        temp = self.head
        while(temp):
            count=count+1
            temp = temp.next
        return count
    
    def getFirst(self):
        return self.head
    
    def getLast(self):
        temp = self.head
        if temp == None:
            return

        while(temp):
            if (temp.next == None):
                return temp
            temp = temp.next
    
    def getAt(self,index):
        if self.head == None:
            return

        count = 0
        temp = self.head
        while(temp):

            if count == index:
                return temp
            count = count + 1
            temp = temp.next

        return None
    
    def removeAt(self, index):
        if self.head == None:
            return

        count = 0
        previous = self.head
        temp = self.head.next

        while(temp):

            if count == 0:
                this.head = this.head.next
                return
            
            previous = getAt(index-1)
            if previous == None or previous.next == None:
                return None
            previous.next = previous.next.next
           
        return None

    def insertAt(self, index, data):
        if self.head == None:
            self.head = Node(data)

        if index == 0:
            self.head = Node(data,self.head)
            return

        previous = self.getAt(index-1) or self.getLast()
        previous.next = Node(data,previous.next)
       

    
    def clear(self):
        self.head = None

    def removeFirst(self):
        temp = self.head
        if temp == None:
            return
        else:
            self.head = temp.next
    
    def removeLast(self):
        temp = self.head
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            return
        
        previous = self.head
        temp = self.head.next
        while(temp):
            
            if(temp.next == None):
                previous.next = None
                return previous
            previous = previous.next
            temp = temp.next


    def insertLast(self,data):
        temp = self.head
        if temp==None:
            self.head = Node(data)
            return

        while(temp):
            if temp.next == None:
                temp.next = Node(data)
                return
            temp = temp.next
        

    def mid(self):
        slow = self.head
        fast = self.head
        if slow == None:
            return
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        return slow

    def isCircular(self):
        slow = self.head
        fast = self.head
        if slow == None:
            return
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False


    
    def display(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next


if __name__ == '__main__':
    sll = SingleLinkedList()
    sll.insertFirst(10)
    sll.insertFirst(20)
   
    print("size is " + str(sll.size()))
    print("getLast() - " + str(sll.getLast().data))
    sll.insertLast(30)
    sll.insertFirst(5)
    sll.display()
    print("**********")
    #sll.removeLast()

    #print(sll.getLast().data)
    
    sll.insertAt(2,100)
    sll.display()

    print("mid ==> " + str(sll.mid().data))
    print("Circular ==> " + str(sll.isCircular()))
    




