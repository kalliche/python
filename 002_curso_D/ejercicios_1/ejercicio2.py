# Le pedimos al usuario que diga una frase
frase = input('Decime una frase y te calculo cuanto tardaria si tuvieras que decirla: ')

# creamos una lista de palabras de la frase (se separan cada vez que haya un espacio)
palabras_separadas = frase.split(' ')

# usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

# En caso de que tarde mas de un minuto en decirlo, le decimos que pare
if cantidad_de_palabras > 120:
    print('para tampoco es un testamento')
    
# calculamos cuento tardaria en decir las palabras y se  las decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y te tardarias {cantidad_de_palabras / 2} segundos en decirlas ')
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos en decirlo ')
