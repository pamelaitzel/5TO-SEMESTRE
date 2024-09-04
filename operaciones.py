# Crear un array 3D
array_3d = np.random.randint(0, 10, size=(3, 3, 3))

# Sumar todos los elementos
suma_total = np.sum(array_3d)

# Calcular el promedio por cada dimensión
promedio_dim_0 = np.mean(array_3d, axis=0)
promedio_dim_1 = np.mean(array_3d, axis=1)
promedio_dim_2 = np.mean(array_3d, axis=2)

print(f"Array 3D:\n{array_3d}")
print(f"Suma total: {suma_total}")
print(f"Promedio por dimensión 0:\n{promedio_dim_0}")
print(f"Promedio por dimensión 1:\n{promedio_dim_1}")
print(f"Promedio por dimensión 2:\n{promedio_dim_2}")