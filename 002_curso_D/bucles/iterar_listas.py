animales = ['gato','perro','loro','cocodrilo']
numeros = [52,16,14,72]

for animal in animales:
    print(f'Ahora la varianble es igual >> {animal} ')
   
# recorriendo lista y multiplicando por 10 
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
for numero, animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero} ')
    print(f'recorriendo lista 2: {animal} ')
    
# forma no optima de recorrer una listacon su indice
for num in range(len(numeros)):
    print(numeros[num])
    
# forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor} ')
    
# usando el else EL ELSE SIEMPRE SE EJECUTA una vez al finalizar el bucle
for numero in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero} ')
else:
    print('El bucle termino')