frase = input('Decime una frase y te calculo cuanto tardaria si tuvieras que decirla: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y te tardarias {cantidad_de_palabras / 2} segundos en decirlas ')
print(f'Dalto lo diria en {cantidad_de_palabras // 2 * 1.3} segundos en decirlo ')

3.05