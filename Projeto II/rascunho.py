def encontrar_indice(numero, lista):
    try:
        indice = lista.index(numero)
        return indice
    except ValueError:
        return None
import numpy as np 
# Exemplo de uso:
numeros = [10, 20, 30, 40, 50]
numero_procurado = 30
indice = encontrar_indice(numero_procurado, numeros)

if indice is not None:
    print(f"O número {numero_procurado} está na lista no índice {indice}.")
else:
    print(f"O número {numero_procurado} não está na lista.")


import numpy as np

# Lista de arrays
lista_de_arrays = [
    np.array([ 2, 12, 13, 26, 29]),
    np.array([10, 17, 21, 21, 30]),
    np.array([ 8,  9, 21, 27, 30]),
    np.array([ 9, 13, 17, 20, 30]),
    np.array([ 6, 21, 22, 24, 30]),
    np.array([ 2,  4,  9, 11, 22])
]

# Remover o último elemento do segundo array (índice 1)
array_removido = lista_de_arrays[1][-1]
lista_de_arrays[1] = np.delete(lista_de_arrays[1], -1)

print("Array removido:", array_removido)
print("Lista atualizada:", lista_de_arrays)

