import numpy as np

# Crear un array de 10 números aleatorios entre 0 y 100
array = np.random.randint(0, 100, size=10)

# Operaciones
max_val = np.max(array)
min_val = np.min(array)
mean_val = np.mean(array)
median_val = np.median(array)
sum_val = np.sum(array)

print(f"Array: {array}")
print(f"Máximo: {max_val}, Mínimo: {min_val}")
print(f"Media: {mean_val}, Mediana: {median_val}")
print(f"Suma: {sum_val}")