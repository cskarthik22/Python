

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

boollis = [True,True,False,True]
print(all(boollis))


def is_palindrome(s):
    return (all(s[i]==s[~i] for i in range(len(s)//2)))

print( is_palindrome('kak'))