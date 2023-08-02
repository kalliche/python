# creando una función que nos devuelva los numeros primos
# entre 0 y el argumento que pasemos

# crear una función que verifique si un numero es primo
def es_primo(num):
    # verificamos que el numero pasado no pueda dividirse
    # por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num -1):
        # si es divisible por alguno retornamos false y termina el bucle
        if num % i == 0:
            return False
    # si termina el bucle, significa que no fue divisible entonces es primo
    return True

# creando función que retorna una lista con todos los primos
def primos_hasta(num):
    # creamos la lista
    primos = []
    for i in range(3, num + 1):
        # verificamos si el valor es primo
        resultado = es_primo(i)
        # en caso de que sea lo agregamos a la lista
        if resultado == True:
            primos.append(i)
    # devolvemos la lista
    return primos

# creamos el resultado llamando a la función y lo mostramos.
resultado = primos_hasta(99)
print(resultado)