import pandas as pd
df = pd.DataFrame({'Grupo': ['A', 'B', 'A', 'B'], 'Valor': [10, 20, 30, 40]})
print(df.groupby('Grupo').mean())
