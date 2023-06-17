### Error types ###

# syntaxError (Error de sintaxis)
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# print'Hola comunidad'  ESTE ES EL ERROR
print('Hola comunidad')

# NameError (La variable no esta definida)
# NameError: name 'varible' is not defined
# print(varible) ESTE ES EL ERROR
variable = 'Soy el mejor'
print(variable)

# IndexError (No hay elemento para ese indice)
# IndexError: list index out of range
my_list = ['Python', 'Swift', 'Klotin', 'Dart', 'JavaScript']
print(my_list[-1])
print(my_list[4])
# print(my_list[5]) #falta elemento para este indice

# ModuleNotFoundError (modulo no encontrado con ese nombre)
# ModuleNotFoundError: No module named 'maths'
# import maths
import math

# AttributeError (El nombre PI no se encuentra en el modulo)
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
# print(math.PI)  # descomentar para el error
print(math.pi)

# KeyError (el nombre del key no es correcto)
# KeyError: 'apelido'
my_dict = {'nombre':'Carlos', 'apellido':'Garcia', 'edad':36, 1:'Python'}
#print(my_dict['apelido'])   # descomentar para el error
print(my_dict['apellido'])

# TypeError (las listas se llama por int y no por string)
# TypeError: list indices must be integers or slices, not str
#print(my_list['-1'])   # descomentar para el error
print(my_list[-1])

# ImportError (no se localiza el nombre del modulo)
# ImportError: cannot import name 'PI' from 'math' (unknown location)
# from math import PI # descomentar para el error
from math import pi
print(pi)

# ValueError (imposible convertir a entero lacadena)
# ValueError: invalid literal for int() with base 10: '10 años'
#my_int = int('10 años')     # descomentar para el error
my_int = int('10')
print(type(my_int))

# ZeroDivisionError
# ZeroDivisionError: division by zero
print(4/2)
#print(4/0)   # descomentar para el error
