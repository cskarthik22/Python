
def RotateLeftByOne(A):
    first = A[0]
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[len(A)-1] = first

def RotateLeft(A,d):
    for i in range(d):
        RotateLeftByOne(A)
    return A


A = [1,2,3,4,5]
print(RotateLeft(A,4))