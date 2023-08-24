import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dispersion.csv')

# creando el grafico
sns.scatterplot(x='mtiempo', y='dinero', data=df)

# mostrando grafica
plt.show()