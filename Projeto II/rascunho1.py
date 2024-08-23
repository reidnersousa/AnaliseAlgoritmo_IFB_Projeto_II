import numpy as np 
import bubble_sort as bb
vetor=bb.gerando_amostra(10*5)
vetor = bb.etapa_1(vetor)
def etapa_3(lista_maiores):
 
  maior_ele = lista_maiores[-1]
 
  print("maior_ele",maior_ele)
  return maior_ele

def etapa_2(vetor):
  lista_maiores = []
  for i in vetor:
   
    maior_elemento = i[-1]
    lista_maiores.append(maior_elemento)
  print("lista_maiores_2",lista_maiores)
  lista_maiores_ordenados = bb.bubbleSort(lista_maiores)
  #print("lista_maiores_2",lista_maiores,lista_maiores_ordenados)
  maior=etapa_3(lista_maiores_ordenados)
 
  indice=bb.encontrar_indice(maior,lista_maiores)
  print(indice)
  vetor[indice] = np.delete(vetor[indice],-1)
  print(vetor)


print("Vetor input",vetor)
etapa_2(vetor)