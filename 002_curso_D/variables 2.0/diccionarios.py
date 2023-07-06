# creando diccionarios con dict()
diccionario = dict(nombre='Carlos', apellido='Garcia')

# las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(['dalto','lucas']): 'si se puede'}

# creando diccionario con fromkeys()
diccionario = dict.fromkeys(['nombre','apellido','suscriptores'])

print(diccionario)
print(type(diccionario))

