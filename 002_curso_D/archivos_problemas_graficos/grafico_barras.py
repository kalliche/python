import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cofla_ingresos.csv')

# creando grafico
sns.barplot(x='fuente', y='ingresos', data=df)

# sumar total de los ingresos
total_ingresos = df['ingresos'].sum()
# mostrar el total de ingresos
print(f'El total de ingresos es de: {total_ingresos}')

# mostrar grafico
plt.show()