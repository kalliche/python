## sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {'Carlos', 'Garcia', 37}
print(type(my_other_set))

print('\nlen cuenta la cantidad de elelementos')
print(len(my_other_set))

print('\nadd agregar elementos al conjuntos')
my_other_set.add(1.75)
print(my_other_set)

print('\nin para evaluar si el elemento existe')
print('Carloss' in my_other_set)
print(37 in my_other_set)

print('\nremove eliminar un elemento por referencia')
print(my_other_set)
my_other_set.remove('Carlos')
print(my_other_set)

print('\nclear elimina todos elementos')
my_other_set.clear()
print(my_other_set)

print('\ndel elimina el objeto del programa')
del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

print('\ncombertir set a lista')
my_set = {'Carlos', 'Garcia', 37}
my_list = list(my_set)
print(type(my_list))
print(my_list)

print('\n unir dos set')
my_other_set = {'javaScript', 'Kotlin', 'Python', 'css'}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union('c++', 'R')) # se agrega elementos pero no se almacena en la variable





'''
1   No es una estructura ordenada
2   no se acceder por index a los elementos
3   los elementos no se repiten
'''