'''
El juego de adivinanzas, es necesario escribir un programa para seleccionar un numero aleatorio entre 1 y 10. Para dar pistas al usuario podemos usar declaraciones condicionales para alertar si el numero es menor o mayoro es igual al numero seleccionado
'''

import random

n = random.randrange(1,10)
guess = int(input('Ingrese cualquier numero: '))
while n != guess:
    if guess < n:
        print('demaciado bajo')
        guess = int(input('Ingrese un numereo nuevamente'))
    elif guess > n:
        print('demaciado alto')
        guess = int(input('Ingrese un numereo nuevamente'))
    else:
        break
print('Lo adivinaste que bien!!!')




'''
guess = adivinar
'''
