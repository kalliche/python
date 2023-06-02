# for
my_list = [35,24,62,52,30,30,17]

my_dict = {
    'nombre': 'Carlos',
    'apellido': 'Garcia',
    'edad': 37,
    'lenguaje':{'Python','Swift','Kotlin'}
    }

my_tuple = (35, 1.65, 'Carlos', 'Garcia')

my_set = {'Carlos', 'Garcia', 37}

print('itera un lista')
for element in my_list:
    print(element)

print('\nItera un diccionario')
for element in my_dict:
    print(element)

print('\nitera un set')
for element in my_set:
    print(element)

print('\nitera una tupla')
for element in my_tuple:
    print(element)

print('\nbreak saliendo del for')
for element in my_dict:
    print(element)
    if element == 'apellido':
        break
else:
    print('El bucle a finalizado')

print('\ncontinue sonto al inicio')
for element in my_dict:
    print(element)
    if element == 'apellido':
        continue
else:
    print('El bucle a finalizado')


