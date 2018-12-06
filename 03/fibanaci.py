import os

os.system('clear') 
def fibanaci(n):
    a = 1
    b = 1
    out = []
    for num in range(n):
        out.append(a)
        t = a
        a = b
        b = t + a
    return out

print(fibanaci(10))

print("========================")

def generator_fibanaci(n):
    a = 1
    b = 1
    for num in range(n):
        yield a
        t = a
        a = b
        b = t + a
for num in generator_fibanaci(10):
    print(num)

print("========================")


    





    

   