# Crear un DataFrame con valores faltantes
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
}
df_nan = pd.DataFrame(data_with_nan)

print("DataFrame con valores faltantes:\n", df_nan)

# Detectar valores faltantes
missing_values = df_nan.isnull()
print("Valores faltantes:\n", missing_values)

# Rellenar los valores faltantes con un número
df_filled = df_nan.fillna(0)
print("DataFrame con valores faltantes reemplazados:\n", df_filled)
