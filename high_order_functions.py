'''
Las funciones de orden mayor, son aquellas que llaman a otra funcion dentro de ella misma.
Las mas conocidas son:

- Filter
- Map
'''

from functools import reduce


# Filter

my_list = [1,4,5,6,9,13,19,21]

odd = list(filter(lambda x: x%2 != 0, my_list))

print(odd)


# Map

my_list2 = [1,2,3,4,5]

squares = list(map(lambda x: x**2, my_list2))

print(squares)


# Reduce

my_list3 = [2,2,2,2,2]

#En este cas, la funcion de lambda toma 2 valores "a" y "b" porque en la primera vuelta toma el primer valor de la lista como a y el segundo como b, ese dato lo guarda como a y el tercer valor toma el tercer valor

all_multiplied = reduce(lambda a, b: a*b, my_list3)

print(all_multiplied)

