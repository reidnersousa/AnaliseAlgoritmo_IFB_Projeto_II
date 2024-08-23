import numpy as np 
import bubble_sort as bb



vetor=bb.gerando_amostra(50)
vetor = bb.etapa_1(vetor)


print("Vetor input",vetor)
vetor=bb.etapa_2(vetor)
print()
print(vetor)

vetor=bb.etapa_2(vetor)
print()
print(vetor)
