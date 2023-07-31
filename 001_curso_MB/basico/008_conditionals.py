### condicionales ###

my_condition = False

if my_condition:
    print('Se ejecuta la condicion del if')

# para que no se ejete la condicion
my_condition = 5 * 2

if my_condition == 11:
    print('no se ejecuta esta condiición')

if my_condition == 10:
    print('tercera condición, esta si cumple')

print('Le ejecución continual')

if my_condition > 10:
    print('Es mayor que 10')
else:
    print('es menor o igual que 10')

print('\n')
my_condition1 = 51
if len(str(my_condition1)) == 1 and my_condition1 < 10:
    print('unidades')
elif len(str(my_condition1)) == 2 and my_condition1 < 100:
    print('decenas')
elif len(str(my_condition1)) == 3 and my_condition1 < 1000:
    print('centenas')
else:
    print('unidades de mil')