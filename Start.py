# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:50:46 2015

@author: Alexandre Lima
"""

# importar função randomica
from random import randint 

#introduz o jogo
print ("\nLet's play Battleship!\n")

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

#tentar fazer umas rodadas
while base[ship_row][ship_colum] == "O":
    # pergunta ao user as coordenadas do barco
    guess_row = int(input("Diga em qual linha está o barco: "))
    guess_col = int(input('Diga em qual coluna está o barco: '))

    if guess_row == ship_row and guess_col == ship_colum:
        print("\nParabéns, você acertou o barco!\n")
        break
    else:
        if guess_row not in range(10)or guess_col not in range(10):
            print ("Oops, escolha algo no oceano.")
        elif base[guess_row][guess_col] == "X":
            print ("Você já selecionou essa coordenada")
        else:
            base[guess_row][guess_col] = "X"
            print("\nPuxa, deu água!\n")
            coluna(base)





