# Crear dos matrices aleatorias de 3x3
matriz1 = np.random.randint(0, 10, size=(3, 3))
matriz2 = np.random.randint(0, 10, size=(3, 3))

# Multiplicar matrices
resultado = np.dot(matriz1, matriz2)

print(f"Matriz 1:\n{matriz1}")
print(f"Matriz 2:\n{matriz2}")
print(f"Resultado de la multiplicación:\n{resultado}")