'''con un = estamos agignando pero no estamos comparando'''

# operadores de comparacion

igual_que = 5 == 6
print(f'igual_que  (5 == 6) es >> {igual_que}')

distinto_de = 5 != 6
print(f'distinto_de  (5 != 6) es >> {distinto_de}')

mayor_que = 5 > 6
print(f'mayor_que (5 > 6) es  >> {mayor_que}')

menor_que = 5 < 6
print(f'menor_que (5 < 6) es  >> {menor_que}')

mayor_igual = 5 >= 6
print(f'mayor_igual  (5 >= 6) es >> {mayor_igual}')

menor_igual = 5 <= 6
print(f'menor_igual  (5 <= 6) es >> {menor_igual}')

# calculos combinados
a = 5
b = 10
c = 20
comparacion = a + b < c
print(comparacion)

out_password = 'CarlosMaestro'
int_password = 'CarlosMaestro'
print(out_password == int_password)