import pandas as pd
df = pd.DataFrame({'Nombre': ['Ana', 'Juan'], 'Edad': [34, 23]})
print(df.sort_values(by='Edad'))