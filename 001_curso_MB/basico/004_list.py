#### list ##

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35,24,62,52,30,30,17]
print(type(my_list))
print(len(my_list))
print(my_list)

my_other_list = [35,1.17, 'Carlos', 'Garcia']
print(type(my_other_list))
print(len(my_other_list))
print(my_other_list)

# acceder a las listas
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_other_list.count(35)) # cunatas vecec se repite en la lista

age, height, name, surname = my_other_list
print(name)
print(surname)
print(age)
print(height)

# concatenar dos listas
print(my_list + my_other_list)

print('\nappend Agregar un elemento (se agrega al final de la lista)')
my_other_list.append('Colombia')
print(my_other_list)

print('\ninsert es adicionar un elemento en la posicion deseada')
my_other_list.insert(0, 'Azul')
print(my_other_list)

print('\nremove eliminar elemento de la lista')
my_other_list.remove('Azul')
print(my_other_list)

print('\nremove si hay dos valores iguales solo elimina un elemento 0 elimina el elemento que sabemos que existe')
print(my_list)
my_list.remove(30)
print(my_list)

print('\npop desapilar elemento de la lista')
print(my_list)
print(my_list.pop())
print(my_list)
print('Guardar el elemento desapilado')
my_pop_elemento = my_list.pop(2)
print(my_pop_elemento)
print(type(my_pop_elemento))

print('\ndel eliminar un elemento de la lista, elimina por indice')
print(my_list)
del my_list[2]
print(my_list)

print('\nclear elimina el contenido de la lista')
print('copy copia la lista')
my_new_list = my_list.copy()
print(my_list)
my_list.clear()
print(f'lista vacia {my_list}')
print(f'lista copiada: {my_new_list}')

print('\nreverse invierte el orden de la lista')
print(my_new_list)
my_new_list.reverse()
print(my_new_list)