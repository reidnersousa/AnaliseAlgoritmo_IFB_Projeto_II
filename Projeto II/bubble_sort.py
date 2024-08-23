import numpy as np

import math 
def gerando_amostra(N):
  sequencia = np.random.randint(1, N + 1, N)
  return sequencia


def eh_multiplo(N,qtd_partes):
  return N % qtd_partes ==0


def modulo_sqrt_n(n):
    floor_sqrt_n = math.floor(math.sqrt(n))
    result = n % floor_sqrt_n
    return result

def bubbleSort(array):
  for i in range(len(array)-1,0,-1):
    #print(i)
    swapped =  False
    for j in range(i):
      #print(">>",i)
      if array[j]>array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break
    return array

### Dividir em k partes , k = \sqrt{N}
## Caso o tamanho do vetor não seja multiplo de sqrt\{N}  a ultima parte terá tamanho (n mod \lfloor \sqrt{n} \rfloor)
def etapa_1(vetor):
  tam_vetor=  len(vetor)
  qtd_partes = np.sqrt(tam_vetor)
  lista =[]
  if tam_vetor % qtd_partes == 0:
   
    j = 0
    for i in range(0,int(qtd_partes)):
      j = j +1
      corte = vetor[int(qtd_partes)*i:int(qtd_partes)*j]
      corte=bubbleSort(corte)
     
      lista.append(corte)
  if not eh_multiplo(tam_vetor,qtd_partes):
    
   
    j = 0
    for i in range(0,int(qtd_partes)):
      j = j +1
      corte = vetor[int(qtd_partes)*i:int(qtd_partes)*j]
     
      lista.append(corte)
     
   
    ultimo_corte = vetor[int(qtd_partes)*j:]
    
    
    lista.append(ultimo_corte)
   
  return lista 



N  = 10*3

vetor = gerando_amostra(N)
print("entrada",vetor)
vetor=etapa_1(vetor)
print(vetor)

