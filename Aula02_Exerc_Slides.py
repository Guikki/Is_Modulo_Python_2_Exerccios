# DESAFIO 1 - ORDENAÇÃO
# - Crie um programa que tem uma lista desordenada no início em uma variável e que ordena essa lista e imprime ela ordenada no final.
# - Use o código abaixo para gerar a lista desordenada:
# from random import randint
# lista = [randint(0,99) for _ in range(100)]
# - Não use funções sort(), min() ou max()

from random import randint
lista = [randint(0,99) for _ in range(100)]

for i in range(len(lista)):
    menor = i
    for j in range(i,len(lista)):
        if lista[j] < lista [menor]:
            menor = j
    lista [i], lista[menor] = lista[menor], lista[i]
    
print (lista)

######################################################################################################################################
