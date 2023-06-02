'''Crear un sistema de autenticación de contraseña basado en la lógica es una pregunta popular en las entrevistas de codificación. Entonces, en la sección a continuación, lo llevare a travéz de cómo crear un sistema de autentifricacion de contraseña usando Python'''

'''
    Autentificación de contraseña usando Python
Para crear un sistema de autentificación de contraseña con Python, debe seguir los pasos mencionado a continuación:

1_ crear un diccionario de nombre de usuariocon sus contraseñas
2_ Luego debe solicitar la entrada del usuario como nombre de usuario utilizando la funciónde entrada en Python
3_ Luego debe usar un modulo getpass en Python para solicitar la entrada del usuario como contraseña, Aqui estamos usando el módulo getpass en lugar de la función de entrada para asegurarnos de que el susario no puede ver lo que escribe en el campo de contraseña.
'''

import getpass
database = {'simon':'123456', 'masias':'654321'}
username = input('Ingrese su usuario: ')
password = getpass.getpass('Ingrese su contraseña: ')
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass('Vuelva a introducir la contraseña: ')
        break
print('verificado')
