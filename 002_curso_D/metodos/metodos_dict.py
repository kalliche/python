'''
key() -> devuelve las claves (tambien sirve para iterar)
get() -> devueve el valor de una clave
clear() -> elimina todos los elementos
pop() -> elimina un elemento
items() -> para iterar el diccionario
'''

diccionario = {
    'nombre': 'Carlos',
    'apellidos': 'Dalto',
    'subd': 1000
}
# key()
claves = diccionario.keys()
print(claves)

# get()
valor_de_error = diccionario.get('valor_que_no_existe')
# cuando la refencia del valor no existe el programa continua es la difereceia del metodo anterior
print(valor_de_error)