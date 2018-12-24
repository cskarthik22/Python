
def reverse(strval,res):
 
    #BASE CASE:
    if(len(strval) == 0):
        print res;
    else:
    # Logic    
        res = strval[0] + res
        strval = strval[1:]
        return reverse(strval,res)

def reverse_new(strval):
 
    #BASE CASE:
    if(len(strval) <= 1):
        return strval;
    else:
    # Logic    
        return reverse_new(strval[1:]) + strval[0]

reverse('karthik','')
print(reverse_new('karthik'))

def swap(A,x,y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def reverse_02(s):
    left = 0
    right = len(s) - 1
    while (left <= right):
        swap(s,left,right)
        left = left + 1
        right = right - 1
    return ''.join(s)
s = 'karthik'
print(list(s))
print(reverse_02(list(s)))











