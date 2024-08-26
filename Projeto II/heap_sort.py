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


# Exibe as heaps
def print_heap(vetor):
    for i, heap in enumerate(vetor):
        print(f"Heap {i+1}: {heap.GETHEAP()}")
        
def etapa_2(vetor):
    maiores_2 = []
    
    vetor = [heap for heap in vetor if len(heap.GETHEAP()) > 0]
    #print_heap(vetor)
   
    # Remover o maior elemento de cada heap e armazenar em maiores_2
    for heap in vetor:
        maiores_2.append(heap.REMOVEHEAP())
    
    #print(maiores_2)
    
    # Criar uma nova heap com os maiores elementos removidos
    nova_heap = Heap(maiores_2)
    #print(nova_heap.GETHEAP())
    
    # Remover o maior elemento da nova heap
    m = nova_heap.REMOVEHEAP()
    #print("m", m, "heap", nova_heap.GETHEAP())
    
    # Inserir os valores de volta nas heaps originais
    for i, heap in enumerate(vetor):
        if i < len(maiores_2):
            #print("Heap antes:", heap.GETHEAP())
            heap.INSERTHEAP(maiores_2[i])
            #print("Heap depois:", heap.GETHEAP(), "i", i, "m", maiores_2[i])
        else:
            break
    return m ,vetor
def etapa_4(vetor):
    vetor_solucao = []
    vetor = etapa_1(vetor)
    while  len(vetor)> 0:
       
        vs,vetor=etapa_2(vetor)
        if vs is not None:
            vetor_solucao.append(vs)
    #print(vetor_solucao)
    return vetor_solucao

import timeit


N = 10**6
vetor = gerando_amostra(N)

qtd_rep =1 
tempo_exc = timeit.timeit(lambda: etapa_4(vetor) , number=qtd_rep )

media =  tempo_exc / qtd_rep
print(media)
