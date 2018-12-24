
'''
A = [1,0,2,0,1,0,3,1,0,2]
             - 
     -      | |    -
 -  | |  -  | |-  | |
| |_| |_| |_| | |_| |
 1 0 2 0 1 0 3 1 0 2

left_arr = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
right_arr= [3, 3, 3, 3, 3, 3, 3, 2, 2, 2]  

'''
def max(a,b):
    return a if a > b else b

def min(a,b):
    return a if a < b else b

def findwater(A):
    size = len(A)
    left = [0]*size
    right = [0]*size
    left[0] = A[0]
    print(left)
    i = 1
    while i < size:
        left[i] = max(left[i-1],A[i])
        i = i + 1

    right[~0] = A[~0]
    i = size -2
    while i >= 0:
        right[i] = max(A[i],right[i+1])
        i = i - 1
    
    i = 0
    TotalWaterStorage = 0
    while i < size:
        TotalWaterStorage = TotalWaterStorage + min(left[i],right[i])-A[i]
        i = i + 1
    print(left)
    print(right)
    return TotalWaterStorage

A = [1,0,2,0,1,0,3,1,0,2]
print(findwater(A))


  
  

