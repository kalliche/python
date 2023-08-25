import re

texto = '''Hola maestro,4 esta es la cadeena 1, como estas mi capitan. _.
Esta es la segunda linea de texto 2 _.
y Esta es la final definitiva mi capitan? 9
1122172313 6900527 123 1234 12345 123456 1234567 12345678 123456789 1234567890, _.
'''

print('----' * 9)
# busca el primer hola
resultado = re.search('Hola', texto)
print(resultado)

print('----' * 9)
# regresa el resultado de todas las busqueda
resultado2 = re.findall('esta', texto)
print(resultado2)

print('----' * 9)
# regresa el resultado de todas las busqueda ingorando mayuscular
resultado2 = re.findall('esta', texto, flags=re.IGNORECASE)
print(resultado2)

print('----' * 9)
# \d busca digitos numericos del 0 - 9
resultado3 = re.findall(r'\d', texto)
print(resultado3)

print('----' * 9)
# \d busca todo menos digitos numericos del 0 - 9
resultado3 = re.findall(r'\D', texto)
print(resultado3)

print('----' * 9)
# \w -> busca caracteres lfanumericos [a-z A-Z 0-9]
resultado4 = re.findall(r'\w', texto)
print(resultado4)

print('----' * 9)
# \W -> busca todo meno caracteres alfabnumericos
resultado5 = re.findall(r'\W', texto)
print(resultado5)

print('----' * 9)
# \s -> busca todo los espacion en blanco espacios, tab, saltos de linea
resultado6 = re.findall(r'\s', texto)
print(resultado6)

print('----' * 9)
# \S -> busca todo meno espacion, tab, saltos de linea
resultado7 = re.findall(r'\S', texto)
print(resultado7)

print('----' * 9)
# . -> busca todo menos salto en linea
resultado8 = re.findall(r'.', texto)
print(resultado8)

print('----' * 9)
# \n -> busca todos los saltos de linea
resultado9 = re.findall(r'\n', texto)
print(resultado9)

print('----' * 9)
# \ -> cancela caracteres especiales, cancela la funcion del punto y busca .
resultado10 = re.findall(r'\.', texto)
print(resultado10)

print('----' * 9)
# armando una cadena que busque un numero, seguido de un guion punto y espacio
resultado11 = re.findall(f'\d\.\s', texto)
print(resultado11)

print('----' * 9)
# busca numeros juntos
resultado12 = re.findall(r'\d{10}', texto)
print(resultado12)

print('----' * 9)
# busca numeros juntos
resultado12 = re.findall(r'\b\d{5,}\b', texto)
print(resultado12)
