
def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


def MaxHeapify(A,index,size):
    left = 2*index
    right = 2*index+1
    greatest = index

    if(left<size and A[left]>A[greatest]):
        greatest = left
    else:
        greatest = index
    
    if(right<size and A[right]>A[greatest]):
        greatest = right
    
    if(greatest != index):
        swap(A,index,greatest)
        MaxHeapify(A,greatest,size)

def convertToHeap(A):
    i = len(A)//2 -1
    while i >=0:
        MaxHeapify(A,i, len(A))
        i = i-1
    return A

def HeapSort(A):
    convertToHeap(A)
    i = len(A)-1
    while i>=0:
        swap(A,0,i)
        MaxHeapify(A,0,i)
        i = i -1
    return A

A = [3,4,1,5,6,7,2]

print(A)        
print(HeapSort(A))