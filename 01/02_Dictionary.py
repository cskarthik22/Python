'''
{ } - Dictionary
help(list)
Mappings - Key, value pair
keys(), values(), items(), 

'''

dic = { }

dic[1] = 'one'
dic[2] = 'two'
dic['a'] = 'apple'
print(dic)
print(dic['a'])

for i in dic.items():
    print(i)
print("===============================")

numbers = { 1 : 'one', 2: 'two', 3 : 'three'}
print( numbers )
print( numbers.keys() )
print( numbers.values() )
print( numbers.items() )

print("===============================")

for key in numbers:
    print key

for k,v in numbers.iteritems(): ## in python 2
    print(v)

for k,v in numbers.items(): ## in python 3
    print(k,v)



