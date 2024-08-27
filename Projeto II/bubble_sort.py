import numpy as np
import timeit

def encontrar_indice(numero, lista):
    try:
        indice = lista.index(numero)
        return indice
    except ValueError:
        return None

def gerando_amostra(N):
    return np.random.randint(1, N + 1, N)

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
    for i in range(qtd_partes):
        j += 1
        corte = vetor[qtd_partes * i:qtd_partes * j]
        corte = bubbleSort(corte)
        lista.append(corte.tolist())  # Converte para lista Python
    
    if j * qtd_partes < tam_vetor:
        ultimo_corte = vetor[j * qtd_partes:]
        ultimo_corte = bubbleSort(ultimo_corte)
        lista.append(ultimo_corte.tolist())  # Converte para lista Python
    
    return lista

def etapa_2(vetor):
    vetor_solucao = []
    while vetor:
        # Encontra o maior elemento no final de cada sublista
        maiores = [sublista[-1] for sublista in vetor]
        maior_valor = max(maiores)
        indice = encontrar_indice(maior_valor, maiores)
        
        # Remove o maior elemento encontrado e adiciona na solução
        vetor_solucao.append(maior_valor)
        vetor[indice].pop()  # Agora funciona porque sublista é uma lista Python
        
        # Remove sublistas vazias
        vetor = [sublista for sublista in vetor if sublista]
    
    return vetor_solucao

def etapa_4(vetor):
    vetor = etapa_1(vetor)
    vetor_solucao = etapa_2(vetor)
    return vetor_solucao

N = 10**7
vetor = gerando_amostra(N)

# Medindo o tempo de execução
qtd_rep = 1
tempo_exc = timeit.timeit(lambda: etapa_4(vetor), number=qtd_rep)
media = tempo_exc / qtd_rep
print(media, N)
