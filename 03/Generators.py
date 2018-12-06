'''
Generator functions allow us to write a function that can send back a value 
and then later resume to pickup where it left off.
This is acheived using Yield keyword.
This function whem compiled it becomes object that support iteration 
protocol
'''
#========PROBLEM #1 ======================
def cubes(n):
    out = []
    for num in range(n):
        out.append(num**3)
    return out

for x in cubes(10):
    print(x)

print("===============================")

def generator_cubes(n):
    # out = []
    for num in range(n):
        #out.append(num**3)
        yield num**3
    #return out

for x in generator_cubes(10):
    print(x)




