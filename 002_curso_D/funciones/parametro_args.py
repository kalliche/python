# utilizando el operador * como argumento (*args)
def suma(nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma('Carlos', 5,3,9,10,20,3)
print(resultado)

# forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([5,3,9,10,20,3])
print(resultado2)