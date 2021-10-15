from functools import reduce
# las funciones de orden superior, son funciones que reciben otra funcion como parametro
# ejemplo filter, map, reduce
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
my_list_reduce = [2, 2, 2, 2, 2, 2, 2]

'''devuelve True or False según el valor esté dentro de 
los criterios buscados o no. En caso de que no cumpla con la condición,
 no será devuelto y la lista se verá reducida por este filtro'''
odd = list(filter(lambda x: x % 2 != 0, my_list))

'''Funciona muy parecido, pero su diferencia radica en que no puede eliminar valores 
de la lista del array entregado. Es decir, el output tiene la misma
 cantidad de valores que el input.'''
odd_map = list(map(lambda x: x**2, my_list))

'''Toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza 
la función con estos 2 valores, y luego con el resultado de esto y el valor 
que le sigue en el array. Y así hasta pasar por todos los valores de la lista.'''
odd_reduce = list(map(lambda a,b: a**b, my_list_reduce))

print(odd)
print(odd_map)
print(odd_reduce)
