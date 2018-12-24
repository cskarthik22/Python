
def BinarySearch(A,left,right,target):

    while( left <= right ):
        mid = left + (right - left)//2
        if A[mid] == target:
            return mid
        if A[mid] < target:
            left = mid + 1
        if A[mid] > target:
            right = mid - 1
    
    return -1

print(BinarySearch([2,3,6,8,12,15,17],0,6,8))






    

