# Crear un array de números aleatorios entre 0 y 50
array = np.random.randint(0, 50, size=15)

# Reemplazar los números mayores a 25 por 100
array[array > 25] = 100

print(f"Array modificado: {array}")