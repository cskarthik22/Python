'''
Similar to Map, reduce(function,sequence)

seq =[s1,s2,s3,s4...]
reduce function takes arguments as (((s1,s2),s3),s4)...
Takes 2 arguments in the sequence and the result is used as first argument in next PASS

'''

numbers = [1,2,3,4,5]

sum = lambda x,y: x+y

'''
Takes 2 arguments in the sequence and the result is used as first argument in next PASS
PASS1: sum(1,2) = 3
PASS2: sum(3,3) = 6
PASS3: sum(6,4) = 10
PASS4: sum(10,5) = 15

'''
print(reduce(sum,numbers))

def max_find(x,y):
    if (x>y):
        return x
    else:
        return y

print(max_find(20,200))

print(reduce(max_find,numbers))

print("========================")

print(reduce(lambda x,y: x if (x>y) else y,numbers))

