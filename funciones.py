def elevar_al_cuadrado(array):
    return np.square(array)

# Crear un array de números enteros
array = np.array([2, 4, 6, 8])

# Aplicar la función
resultado = elevar_al_cuadrado(array)

print(f"Array original: {array}")
print(f"Array al cuadrado: {resultado}")