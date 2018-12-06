
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

boollis = [True,True,False,True]
print(any(boollis))


def is_present(s,ch):
    return (any(s[i]==ch for i in range(len(s))))
        
print(is_present('python','y'))

