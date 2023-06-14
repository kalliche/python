### challenges ###

'''
Escribe un programa que muester por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresión), sustituyendo lo siguiente:
    - multiplos de 3 por la palabra 'fizz'
    - multiplos de 5 por la palabra 'buzz'
    - mulplos de 3 y de 5 a la vez por la palabra 'fizzbuzz'
'''

def fizzbuzz():
     for index in range(1,101):
        if index % 3 == 0 and index % 5 == 0:
            print('fizzbuzz')
        elif index % 3 == 0:
            print('fizz')
        elif index % 5 == 0:
            print('buzz')
        else:
            print(index)
fizzbuzz()

'''
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (string) y retorne verdadero o falso (boll) según sean o no anagramas.
    - Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial.
    - No hace falta comprobar que ambas palabras axistan.
    - Dos palabras exactamente iguales no son anagramas
'''

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
print(is_anagram('Amor', 'Roma'))


'''
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesin de fibonacci empezando en 0
    - la serie de Fibonacci se compone por una sucesion de números en la que el siguiente siempre es la suma de los dos anteriores.
    0,1,1,2,3,5,8,13...
'''

def fibonacci():
    prev = 0
    next = 1
    for index in range(1, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
fibonacci()


'''
¿ES UN NÚMERO PRIMO?
Escribir un programa que se encargue de comprobar si un número es primo o no primo,
Hecho esto, imprime los números primos entre 1 y 100
'''

def is_prime():
    for number in range(1,101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index  == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)
is_prime()


'''
INVERTIR CADENA
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automatica,
    - Si le pasamos 'Hola mundo' nos retornaria 'odnum plaH'
'''

def reverse(text):
    text_len = len(text)
    reverse_text = ''
    for index in range(0, text_len):
        reverse_text += text[text_len - index -1]
    return reverse_text
print(reverse('Hola mundo'))