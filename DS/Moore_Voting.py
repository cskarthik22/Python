
def getMajorityElement(A):
    majorityIndex = 0
    count = 1
    i = 1
    while i < len(A):
        if A[i] == A[majorityIndex]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            majorityIndex = i
            count = 1

        i = i + 1
    return A[majorityIndex]

def isMajority(A, majorityElement):
    count = 0
    for val in A:
        if val == majorityElement:
            count = count + 1
    return True if count > len(A)//2 else False

lis =[1,2,1,3,1,1,3]
element = getMajorityElement(lis)
print(element, isMajority(lis,element))

        
