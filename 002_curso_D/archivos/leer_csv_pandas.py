import pandas as pd

# usando la funcion read.csv para leer el archivo csv
df = pd.read_csv('datos.csv', names=['name','lastname','age'])
df2 = pd.read_csv('datos.csv', names=['name','lastname','age'])
print(df)

print('--'*30)
# onteniendo los catos de la columna nombre
print(df["name"])

print('--'*30)
cadena = '0123456789'
print(cadena[2:6])

print('--'*30)
# ordenar columna por edad
df_ordenado_ascendente = df.sort_values('age')
print(df_ordenado_ascendente)

print('--'*30)
# ordenarlo de forma desendente
df_ordenado_descendente = df.sort_values('age', ascending=False)
print(df_ordenado_descendente)

print('--'*30)
# concatenar los dos tadaframe
df_concatenado = pd.concat([df,df2])
print(df_concatenado)

print('--'*30)
# accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)
print(primeras_filas)

print('--'*30)
# accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)
print(ultimas_filas)

print('--'*30)
# accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape
print(f'Son {columnas_totales} columnas y ,{filas_totales} filas')

print('--'*30)
# obteniendo data estadistica del dataframe
df_info = df.describe()
print(df_info)

print('--'*30)
#accediendo a un elemento especifico del df con loc
elementos_especificos_loc = df.loc[2,'age']
print(df)
print(elementos_especificos_loc)

print('--'*30)
# accediendo  a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)

print('--'*30)
# accediendo a todas las fiilas de una columna
apellidos = df.iloc[:,1]
print(apellidos)

print('--'*30)
# accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]
print(fila_3)
print('--'*30)
fila_4 = df.iloc[2,:]
print(fila_4)

print('--'*30)
# accediendo a filas con edad mayor a 30
mayor_que_30 = df.loc[df["age"]== 2,:]
print(mayor_que_30)
