## bucles
# sirve para pasar por el mismo codigo varias veces

# while -> mientras
my_codition = 0

while my_codition < 5:
    print(my_codition)
    my_codition += 1
else:
    print('mi condicion es mayor o igual que 10')
print('La ejecusción continua')

while my_codition < 20:
    my_codition += 1
    if my_codition == 15:
        print('Se detiene la ejecución')
        break

    print(my_codition)