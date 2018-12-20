'''
[ ] - LISTS
help(list)
List are Dynamic arrays & are of linear data structure.
append(), pop(), reverse(), sort()

'''

lis = []
lis = lis + [1]
lis = lis + [2]
lis = lis + [3]
lis += ['one']
lis += ['two']
lis += ['three']
print(lis)

for i in lis[2:]:
    print(i)


print('=================================')

numbers = [1,2,3,'one','two','three']
print(numbers)
print(numbers[:])
print(numbers[:2])
print(numbers[2:])
print(numbers[2:4])
numbers.append('xyz')
print(numbers)
print('=================================')
numbers.pop();
print(numbers)
numbers.pop(0);
print(numbers)

print('=================================')
val = list('python')
print(val) # like split string to a array of characters
val.reverse()
print(val)
print(val[::-1])
val.sort()
print(val)
print(val*3)

print('=================================')
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

matrix = [a,b,c]
print(matrix)
print(matrix[1])
print(matrix[1][2])
print(matrix*2)






