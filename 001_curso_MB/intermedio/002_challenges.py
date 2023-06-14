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
    #
    return True

is_anagram()