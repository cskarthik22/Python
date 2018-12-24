print '%s for %s' %('a', 'apple')
print '{x} + {y} is {z}'.format(x=2,y=3,z=5)

a = 2
b = 3

print('%.6f' %(a*1.0/b))
res = '%.6f' %(a*1.0/b)
print(res)

s = '07:05:45PM'
timelis = s.split(':')
if s[-2:] == 'AM':
    res ='%s:%s:%s' %(timelis[0],timelis[1],timelis[2][:-2])
if s[-2:] == 'PM':
    res ='%s:%s:%s' %(int(timelis[0])+12,timelis[1],timelis[2][:-2])

print(res)
print(s[:-2])
print(s[-2:])
import sys
print(''.join(sorted(sys.argv[1])))

N = int(input())
print('input is %d' %(N))