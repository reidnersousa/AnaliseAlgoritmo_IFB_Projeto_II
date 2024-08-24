import heapq
import numpy as np 
class Heap:
    def __init__(self, vetor=None):
        if vetor is None:
            self.heap = []
        else:
            self.heap = vetor
            self.MAKEHEAP()

    def MAKEHEAP(self):
        # Transforma o vetor em uma heap
        heapq.heapify(self.heap)

    def INSERTHEAP(self, x):
        # Insere o elemento x na heap
        heapq.heappush(self.heap, x)

    def REMOVEHEAP(self):
        # Remove e retorna o maior elemento da heap
        if len(self.heap) > 0:
            # Usamos a função nlargest para obter o maior elemento
            max_element = heapq.nlargest(1, self.heap)[0]
            self.heap.remove(max_element)
            heapq.heapify(self.heap)  # Reestruturamos a heap
            return max_element
        else:
            return None  # A heap está vazia

    def GETHEAP(self):
        # Retorna a heap atual
        return self.heap


def gerando_amostra(N):
    sequencia = np.random.randint(1, N + 1, N)
    return sequencia

def etapa_1(vetor):
    tam_vetor = len(vetor)
    qtd_partes = int(np.sqrt(tam_vetor))
    lista = []
    j = 0
    for i in range(0, qtd_partes):
        j += 1
        corte = vetor[qtd_partes * i:qtd_partes * j]
        corte =list(corte)
        heap = Heap(corte)
        lista.append(heap)
    
    if j * qtd_partes < tam_vetor:
        ultimo_corte = vetor[j * qtd_partes:]
        ultimo_corte = list(ultimo_corte)
        heap = Heap(ultimo_corte)
        lista.append(heap)

    return lista



N = 10**1
vetor = gerando_amostra(N)
print(vetor)
vetor=etapa_1(vetor)



# Exibe as heaps
for i, heap in enumerate(vetor):
    print(f"Heap {i+1}: {heap.GETHEAP()}")
    print(heap.REMOVEHEAP())