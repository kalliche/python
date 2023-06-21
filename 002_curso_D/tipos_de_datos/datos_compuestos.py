'''Listas se puede modificar'''
lista = ['Carlos Garcia', 'Soy caliche', True, 1.65]
print(lista)
print(lista[0])

'''Tuplas: no se puede modificar, solo iterar'''
tupla = ('Carlos Garcia', 'Soy caliche', True, 1.65)

'''set o tambien llamado conjunto son conjuntos desordenados y pueden cambiar, no permite repetir nombres, no hay datos publicados, son datos desordenados, no se puede acceder por el indice'''
conjunto = {'Carlos Garcia', 'Soy caliche', True, 1.65}
print(conjunto) 

'''Crear un diccionario, conformado de key y value, se busca la refencia o por nombre o llave, para llamar a un elemento'''
diccionario = {
    'nombre': 'Carlos Garcia',
    'canal': 'youtube',
    'Estas emocionado': True,
    'altura': 1.65
}
print(diccionario['nombre'])
