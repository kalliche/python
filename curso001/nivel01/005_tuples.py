## tuplas ###
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.65, 'Carlos', 'Garcia')
print(my_tuple)
print(type(my_tuple))

print('\nacceder a los elementos')
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])

print('\ncount cuenta en numero de veces que ase repite un elemento')
print(my_tuple.count(35))

print('\nindex devuelve la ubucacion del elemento que se pasa por parametro')
print(my_tuple.index('Garcia'))


'''
1   las tuplas son inmutables podemos guardar los valores cerrados
    no se puede agregar, modificar
2   se las puede sumar para tener una nueva tupla


'''