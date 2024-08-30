import heapq
import numpy as np

def etapa_1(vetor):
    tam_vetor = len(vetor)
    qtd_partes = int(np.sqrt(tam_vetor))
    lista = []
    j = 0
    for i in range(0, qtd_partes):
        j += 1
        corte = list(vetor[qtd_partes * i:qtd_partes * j])
        heapq.heapify(corte)
        lista.append(corte)
    
    if j * qtd_partes < tam_vetor:
        ultimo_corte = list(vetor[j * qtd_partes:])
        heapq.heapify(ultimo_corte)
        lista.append(ultimo_corte)

    return lista

def etapa_2(vetor):
    maiores_2 = []
    vetor_solucao =  []
    heap_m = [(heapq.heappop(heap),i) for i,heap in enumerate(vetor)]
    heapq.heapify(heap_m)
    while(len(heap_m)):
        value,idx = heapq.heappop(heap_m)
        vetor_solucao.append(value)
        if(len(vetor[idx])>0):
            value2 = heapq.heappop(vetor[idx])
            heapq.heappush(heap_m,(value2,idx))
        
    return vetor_solucao


def gerando_amostra(N):
    sequencia = np.random.randint(1, N + 1, N)
    return sequencia

import timeit


N = 10**7S
vetor = gerando_amostra(N)
#print("Vetor inicial:", vetor)
qtd_rep = 1
vetor = etapa_1(vetor)
#vetor_solucao=etapa_2(vetor)
#print(vetor_solucao)
tempo_exc = timeit.timeit(lambda: etapa_2(vetor), number=qtd_rep)

media = tempo_exc / qtd_rep
print("Tempo médio:", media,N)
