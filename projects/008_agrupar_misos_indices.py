'''Para agrupar elementos del mismo índice, inicialmente tendrá dos o más listas dentro de una lista como [ [ a, b ], [ c, d ] ]. Para agrupar los elementos de estas listas, debe crear dos nuevas listas donde almacenará los elementos de ambas listas en el índice 0 [ a, c ] e índice 1 [ b, d ]. Ese es el significado de agrupar los elementos de los mismos índices.'''

input_list = [[10,20,30],[40,50,60],[70,80,90]]
output_list = []
index = 0

for i in range(len(input_list[0])):
    output_list.append([])
    for j in range(len(input_list)):
        output_list[index].append(input_list[j][index])
    index = index + 1
a,b,c = output_list[0], output_list[1], output_list[2]
print(a,b,c)
