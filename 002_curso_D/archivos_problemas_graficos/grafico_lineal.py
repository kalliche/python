import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# leer el archivo csv
df = pd.read_csv('agua.csv')
print(df)

# hacer la grafica'
sns.lineplot(x='fecha', y='vasos_agua', data=df)

# marcar punto mas alto
plt.plot('01-09',17,'o')

# mostrar grafica
plt.show()
