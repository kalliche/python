'''
LIST -> crea una lista

LEN -> cuenta la catidade de elementos de una lista

APPEND -> agrega un elemento a la lista
INSERT -> agrga un elemento a la lista en el indice especificado
EXTEND -> agregar varios elementos a la lista

POP -> elimina un elemento de una lista, pide el indice y revuelve valor
REMOVE -> remueve un elemento de una lista, pide valor
CLEAR -> elimina todos los elementos de una lista

SORT -> ordena una lista de forma ascendente a descendente
REVERSE -> invierte los elementos de una lista
'''

#  creando una lista con list()
lista = list(['hola', 'Carlos', 35])
print(lista)

# cuenta los elementos de la lista
resultado = len(lista)
print(resultado)

# agregando elemento con appen, se llama a lista mas no a la variable
agregando_con_appen = lista.append(1.65)
print(lista)

# inserta un elemento en la posicion especifica, solicita dos parametros
agregando_con_insert = lista.insert(3,'Masculino')
print(lista)

#gregando valior elementos a la lista se los agrega dentro de corchetes
agregando_con_extend = lista.extend([True,'exitos',2023])
print(lista)

# eliminando un elemento de la lista por su indice
eliminando_con_pop = lista.pop(-2)
print(lista)

# remueve un elemento de la lista por su valor
eliminando_con_remove = lista.remove('hola')
print(lista)

# elimina toda la lista
'''
eliminando_con_clear = lista.clear()
print(lista)
devuelve lista vacio por que se eliminaron sus elementos
'''

lista_num = [12, 56, 1, 90, 65, 42]
# ordena los elementos de una lista
ordenas_con_sort = lista_num.sort()
print(lista_num)

# invierte el orden de la lista
ordenar_con_reverse = lista_num.reverse()
print(lista_num)
