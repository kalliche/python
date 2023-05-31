'''La media es el valor promedio de todos los valores en un conjunto de datos. la suma de todos los valores y luego devidir por la suma de todos lo valores'''

# Media
list1 = [12,16, 20,20,12,30,25,23,24,20]
mean = sum(list1)/len(list1)
print(f'las media de {list1} es {mean}')


'''La mediana  es al valor medio entre todfos los valores en orden ordenado,
1   cuando el número total de valores es par: Mediana = [ ( n / 2 )th término + { ( n / 2 ) + 1 }th] / 2
2   cuando el número total de valores es impar: Mediana = { ( n + 1 ) / 2 }thtérmino
'''
# mediana
list2 = [12,16, 20,20,12,30,25,23,24,20]
list2.sort()

if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2 -1]
    mediana = (m1 + m2)/2
else:
    mediana = list2[len(list2)//2]
print(f'la mediana de la lista es {mediana}')


'''La moda es el valor mas frecuente entre todos los valores'''
# la moda
list3 = [12,16, 20,20,12,30,25,23,24,20]
freciencia = {}

for i in list3:
    freciencia.setdefault(i,0)
    freciencia[i]+=1
frecuente = max(freciencia.values())
for i, j in freciencia.items():
    if j == frecuente:
        moda = i
print(moda)