import heapq
import numpy as np

class MaxHeap:
    def __init__(self, vetor=None):
        if vetor is None:
            self.heap = []
        else:
            self.heap = [-x for x in vetor]  # Negando os valores para transformar em max-heap
            heapq.heapify(self.heap)

    def REMOVEHEAP(self):
        if len(self.heap) > 0:
            return -heapq.heappop(self.heap)  # Retorna o maior elemento original (invertendo o sinal)
        else:
            return None

    def GETHEAP(self):
        return [-x for x in self.heap]

def etapa_1(vetor):
    tam_vetor = len(vetor)
    qtd_partes = int(np.sqrt(tam_vetor))
    lista = []
    j = 0
    for i in range(0, qtd_partes):
        j += 1
        corte = vetor[qtd_partes * i:qtd_partes * j]
        heap = MaxHeap(corte)
        lista.append(heap)
    
    if j * qtd_partes < tam_vetor:
        ultimo_corte = vetor[j * qtd_partes:]
        heap = MaxHeap(ultimo_corte)
        lista.append(heap)

    return lista

def etapa_2(vetor):
    maiores_2 = []
    
    vetor = [heap for heap in vetor if len(heap.GETHEAP()) > 0]

    # adiciona os maiores elementos de cada heap à lista maiores_2
    for heap in vetor:
        maior = heap.REMOVEHEAP()
        if maior is not None:
            maiores_2.append(maior)
    
    # verifica se a lista maiores_2 não está vazia
    if maiores_2:
        m = max(maiores_2) 
        maiores_2.remove(m)
    else:
        return None, vetor
    
    for i, heap in enumerate(vetor):
        if i < len(maiores_2):
            heapq.heappush(heap.heap, -maiores_2[i])  
        else:
            break
    
    return m, vetor

def etapa_4(vetor):
    vetor_solucao = []
    vetor = etapa_1(vetor)
    while len(vetor) > 0:
        vs, vetor = etapa_2(vetor)
        if vs is not None:
            vetor_solucao.append(vs)
    #print("vetor_solucao",vetor_solucao)
    return vetor_solucao

def gerando_amostra(N):
    sequencia = np.random.randint(1, N + 1, N)
    return sequencia

import timeit

N = 10**6
vetor = gerando_amostra(N)
#print("Vetor inicial:", vetor)
qtd_rep = 1
tempo_exc = timeit.timeit(lambda: etapa_4(vetor), number=qtd_rep)

media = tempo_exc / qtd_rep
print("Tempo médio:", media,N)
