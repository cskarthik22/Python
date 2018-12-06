

lst = list('python')
print(lst)


lst = [char for char in 'python']
print(lst)

squares  = [ num**2 for num in range(10)]
print (squares)
even_squares  = [ num**2 for num in range(10) if num%2==0]
print(even_squares)
step2_squares  = [ num**2 for num in range(0,10,2)]
print(step2_squares)
cubes  = [ num**3 for num in range(10)]
print(cubes)

help(list)