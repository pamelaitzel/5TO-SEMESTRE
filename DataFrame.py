import numpy as np
import pandas as pd

# Crear un array NumPy de 3x3
data = np.random.rand(3, 3)

# Crear un DataFrame a partir del array NumPy
df = pd.DataFrame(data, index=['Fila1', 'Fila2', 'Fila3'], columns=['Columna1', 'Columna2', 'Columna3'])

print(df)
