## diccionarios
'''estructura de datos donde podemos guardar valores clave valor'''

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    'nombre': 'Carlos',
    'apellido': 'Garcia',
    'edad': 37,
    1:'Python'
    }
print(my_other_dict)

my_dict = {
    'nombre': 'Carlos',
    'apellido': 'Garcia',
    'edad': 37,
    'lenguaje':{'Python','Swift','Kotlin'}
    }

print(my_dict)
print(my_other_dict)

print('\nlen para conocer cuantos elementos hay')
print(my_dict)
print(my_other_dict)

print('\ncomo acceder a los elementtos')
print(my_dict['nombre'])

print('\nactualizar los elementos del diccionario')
my_dict['nombre'] = 'Reinaldo'
print(my_dict)

print('\nAgregar un nuevo elemento al diccionario')
my_dict['calle'] = 'calle reserva'
print(my_dict)

print('\neliminar un elemento')
print(my_dict)
del my_dict['calle']
print(my_dict)

print('\nvalidar si un elemento existe')
print('carlos' in my_dict)
print('Carlos' in my_dict)

print('\naccedemor a los elementos')
print(my_dict.items())
print('\naccedemor a las llaves')
print(my_dict.keys())
print('\naccedemor a los valores')
print(my_dict.values())

print('****' * 5)

print(my_dict)
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)
my_new_dict = dict.fromkeys(('nombre', 1, 'oiso'))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
