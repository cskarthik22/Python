def even_check(num):
    if (num%2==0):
        return True
    else:
        return False


result = filter(even_check, range(10))
print(result)

print("=========================")

print(filter(lambda num: num%2 ==0,range(10)))
print(filter(lambda num: num%2 ==0 and num>2,range(10)))
print(filter(lambda num: num%2 ==0 or num>3,range(10)))


