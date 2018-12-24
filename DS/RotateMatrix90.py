

A = [ [1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16] ]

def reverseList(A):
    x =0
    for i in A:
        y = 0
        for j in i:
            temp = i[y]
            i[y] = i[~y]
            i[~y] = temp
            y = y+1
        x = x+1
        
    return A

print(reverseList(A))
    