numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

# creando una función lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x * 2
print(multiplicar_por_dos(5))

#creando una función comun que diga si es par o no
def es_par(num):
    if (num % 2 == 1):
        return True

# utilizando filter con una función comun
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))

# creando funacion anterior pero conlambda
pares_numeros = filter(lambda numero: numero % 2 == 0, numeros)
print(list(pares_numeros))