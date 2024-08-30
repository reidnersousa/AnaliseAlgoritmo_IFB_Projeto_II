import numpy as np
import math
import timeit

def encontrar_indice(numero, lista):
    try:
        indice = lista.index(numero)
        return indice
    except ValueError:
        return None

def gerando_amostra(N):
    sequencia = np.random.randint(1, N + 1, N)
    return sequencia

def eh_multiplo(N, qtd_partes):
    return N % qtd_partes == 0

def bubbleSort(arr):
    arr = arr.copy()  # Cria uma cópia para não alterar a lista original
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def etapa_1(vetor):
    tam_vetor = len(vetor)
    qtd_partes = int(np.sqrt(tam_vetor))
    lista = []
    j = 0
    for i in range(0, qtd_partes):
        j += 1
        corte = vetor[qtd_partes * i:qtd_partes * j]
        corte = bubbleSort(corte)
        lista.append(corte)
    
    if j * qtd_partes < tam_vetor:
        ultimo_corte = vetor[j * qtd_partes:]
        ultimo_corte = bubbleSort(ultimo_corte)
        lista.append(ultimo_corte)
    
    return lista

def sort_pedacos(vetor):
    lista = []
    for i in vetor:
        lista.append(bubbleSort(i))
    return lista

def etapa_2(vetor):
    vetor_solucao = []

    while any(len(v) > 0 for v in vetor):  # Continua enquanto houver elementos em qualquer sublista
        maior = -10000000
        idx_maior = -1

        for i, v in enumerate(vetor):
            if len(v) == 0:
                continue
            if v[-1] > maior:
                maior = v[-1]
                idx_maior = i

        vetor_solucao.append(maior)
        vetor[idx_maior] = vetor[idx_maior][:-1]  # Remove o maior elemento encontrado
    print(vetor_solucao,vetor)
    

N = 10**1

vetor = gerando_amostra(N)
vetor = etapa_1(vetor)
print(vetor)

import timeit

qtd_rep = 1
tempo_exc = timeit.timeit(lambda: etapa_2(vetor), number=qtd_rep)
media = tempo_exc / qtd_rep
print(media, N)