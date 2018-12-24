import sys

result = 0
print sys.argv[1:]
for i in sys.argv[1:]:
    result = result + int(i)

print result

a ='how long are the words in this phrase'

def wordlist(iterator):
    lis = []
    strsize = { }
    val = ''
    size = 0
    for char in iterator:
        
        if char == ' ' :
            lis = lis + [val]
            strsize[val] = len(val)
            val = ''
        else:
            val = val + char
    lis = lis + [val]
    strsize[val] = len(val)
    print strsize
    return strsize

res = wordlist(a)
for k in res.iteritems()
    print(k)


print(wordlist(a))



