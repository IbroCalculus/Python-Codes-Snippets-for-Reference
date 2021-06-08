
#Map function applies a function to each item in an iterable (ie, lists, tuples etc)

#map(function, iterable)

list_of_nums = [2,3,4,5,6,7,8,8]
square_func = lambda z: z**2
square_value = map(square_func, list_of_nums)
#print(list(square_value))

print('\n=============')

for i,j in zip(list_of_nums, square_value):
    print(f'{i} -- {j}')
