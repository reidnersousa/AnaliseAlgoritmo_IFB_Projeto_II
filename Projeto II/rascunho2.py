import numpy as np

# Lista de arrays
lista_de_arrays = [
    np.array([ 6, 49, 33, 44, 47, 30, 38]),
    np.array([47, 19, 25,  6,  6, 40,  3]),
    np.array([ 7, 23, 24, 47, 15, 20, 23]),
    np.array([44,  6,  6, 21, 35, 39, 33]),
    np.array([25, 42, 46, 28, 26,  2, 50]),
    np.array([32,  3, 25, 14, 50, 43,  4]),
    np.array([38, 47,  4, 47, 32, 17, 31]),
    np.array([], dtype='int32')
]

# Lista para armazenar os maiores elementos removidos
maiores_elementos = []

# Iterar sobre cada subarray
for i, arr in enumerate(lista_de_arrays):
    if arr.size > 0:  # Certificar que o array não está vazio
        maior_elemento = np.max(arr)  # Encontrar o maior elemento
        maiores_elementos.append(maior_elemento)  # Adicionar o maior elemento à lista
        # Remover o maior elemento da sublista
        lista_de_arrays[i] = np.delete(arr, np.argmax(arr))

# Encontrar o maior entre os elementos removidos
maior_de_todos = max(maiores_elementos)

print("Maiores elementos removidos de cada sublista:", maiores_elementos)
print("Maior elemento removido:", maior_de_todos)
print("Lista de arrays atualizada:", lista_de_arrays)
