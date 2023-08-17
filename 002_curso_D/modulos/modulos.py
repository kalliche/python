# importando un modulo y asignandole nombre m_saludat
# import modulo_saludar as m_saludar

# desde el modulo importamos dis funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal, saludar_rado as saludar_good
import modulo_saludar as m_saludar

# creamos las variables con los saaludos
saludo = saludar_normal('Carlos')
saludar_raro = saludar_good('Simon')

# mostrando los resultados
print(saludo)
print(saludar_raro)

#pare ver las propiedades y metodos de el namespace
print(dir(m_saludar))

#accedemos al nombre del modulo llamado
print(m_saludar.__name__)

# accedemos al nombre de este modulo
print(__name__)

# llmar pero desde un directorio si el modulo esta en un directorio de la misma ruta
from funciones_master.funciones_master import saludando_master as sal_master

saluda = sal_master('Humano')
print(saluda)
print('--' * 20)

# importar desde un directorio fuera del directorio raiz
import sys

# imprime los nombre de los modulos
print(sys.builtin_module_names)

# imprime la ruta de los modulo
print(sys.path)

print('--' * 20)
sys.path.append('/home/carlos-garcia/developer/python/002_curso_D')
#import funciones.crear_funciones
from funciones.crear_funciones import crear_contraseña_random as pass_random

contraseña = pass_random(456)
print(contraseña)
