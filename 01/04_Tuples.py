'''
Tuples are similar to lists, however, unlike lists they are immutable meaning they cannot be changed
e.g: we use to represent days of the week or dates on calendar..etc

.index(val), .count(val), len()
'''

t = (1,2,3,'two', 1,'one','two','two')

print(t)
print(t[3])
print(t.index('one'))
print(t.count('two'))

lis = [(2,4),(6,8),(10,12)]

for tup in lis:
    print tup

for (t1,t2) in lis:
    print t2

