frutas = ['banano', 'manzana', 'ciruela', 'pera', 'naranja', 'granada', 'durazno']
cadena = 'Hola mundo'
numeros = [2,5,2,10]

# desaparece fruta que se come
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(fruta)
    
for fruta in frutas:
    if fruta == 'naranja':
        break
    print(f'las frutas son {fruta} antes de break ')
print('bucle terminado')

#recorree una cadena (iterar)
for letra in cadena:
    print(letra)
    
# for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x * 12 for x in numeros]
print(numeros_duplicados)