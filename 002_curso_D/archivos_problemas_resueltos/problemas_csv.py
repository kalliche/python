# cambiar tipo de datos de una columna
import pandas as pd
df = pd.read_csv('datos.csv')
print(df)

print('---'* 9)
# convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)
print(type(df['edad'][0]))

print('---'* 9)
# cambiando los datos 'dalto' por 'maestro'
df['apellido'].replace('dalto','maestro',inplace=True)
#print(df['apellido'])
print(df)

print('---'* 9)
# eliminando filas con datos faltantes
df = df.dropna()

print('---'* 9)
# eliminar filas repetidas
df = df.drop_duplicates()
print(df)

print('---'* 9)
# creando un csv con el dataframe resultante (limpio)
df.to_csv('datos_limpios.csv')
