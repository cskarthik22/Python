print(complex(2,3))

a ='how long are the words in this phrase'

def wordlist(iterator):
    lis = []
    val = ''
    for char in iterator:
        if char == ' ':
            lis = lis + [val]
            val = ''
        else:
            val = val + char
    lis = lis + [val]
    return lis

print(map(lambda T: len(T), wordlist(a)))

letter = 'h'
print(map(lambda T: len(T),a.split()))

print(filter( lambda T: T[0] == letter,a.split()))

print(globals())
