# creando un conjunto con set()
conjunto = set(['dato 1', 'dato 2'])
print(conjunto)
print(type(conjunto))
print('-*-' * 5)

# metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato 1','dato 2'])
conjunto2 = {conjunto1, 'dato 3'}
print(conjunto2)
print('-*-' * 5)

# teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}
# verificamos si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado1 = conjunto2 <= conjunto1
print(resultado1)
print(resultado)
# verificamos si es un superconjunto
resultado2 = conjunto2.issuperset(conjunto1)
resultado3 = conjunto2 > conjunto1
print(resultado2)
print(resultado3)
# verificar si hay algún número en comun con un elemento que sea comun ya es falso
resultado4 = conjunto2.isdisjoint(conjunto1)
print(resultado4)


print('-*-' * 5)
