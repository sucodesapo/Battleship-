# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:50:46 2015

@author: Alexandre Lima
"""
# importar função randomica
from random import randint 

#criando a base para o brinquedo
base = []

'''
com o looping, eu vou adicionar itens à lista e fica assim:
[ base[0] == ['O', 'O', 'O', 'O', 'O']... base[9] == ['O', 'O', 'O', 'O', 'O'] ] 
'''

for i in range(10):
    while i < 10:
        base.append(["O"]*10)
        break

# criar função para que mostre a lista por colunas
def coluna(base):
    for t in base:
        # tira as virgulas e deixa o jogo mais bonito
        print ('  '.join(t))
coluna(base)

# selecionar um ponto aleatório para esconder o barco
def random_row(base):
    return randint(0,9)
    
def random_colum(base):
    return randint(0,9)
    
ship_row = random_row(base)
ship_colum = random_colum(base)
print(ship_row)
print(ship_colum)

# pergunta ao user as coordenadas do barco
guess_row = int(input("Diga uma linha: "))
guess_col = int(input("Diga uma coluna: "))


if guess_row == ship_row and guess_col == ship_colum:
    print("Acertou")
else:
    print("Água")





