'''
SYNTAX: map(function, sequence) / map(lambda , sequnce) / map(lambda , sequnce1, sequence2...)

'''

def cube(n):
    return n**3;

print(cube(2));

numbers = [1,2,3,4,5]
print(map(cube,numbers))
result = map(cube,numbers)
print(result)

print("=====================")

l_cube = lambda T: T**3
print(map(l_cube,numbers))

print("=====================")

print(map(lambda T: T**3,numbers))

print("=====================")
print(map(lambda n1,n2: n1*n2,numbers,numbers))

print("=====================")
a = [1,2,3,4,5]
b = [10,20,30,40,50]
## Add two lists
print(map(lambda x,y: x+y,a,b))

print(map(lambda T: T**3,range(10)))


