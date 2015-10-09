# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:50:46 2015

@author: Alexandre Lima
"""

#importa o arquivo com os barcos
import leitura

# importar função randomica
from random import randint 

#introduz o jogo
print ("\nBem vindo ao jogo batalha naval, um dos melhores jogos produzidos - agora em versão virtual(escrever mais explicações sobre o jogo)\n")

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

# selecionar os eixos x e y para esconder o barco
def linha_aleatoria(base):
    return randint(0,9)
    
def coluna_aleatoria(base):
    return randint(0,9)
    
eixo_x = linha_aleatoria(base)
eixo_y = coluna_aleatoria(base)

# mostra onde o barco está
print(eixo_x)
print(eixo_y)

#placar
erros = 0
acertos = 0

#tentar fazer umas rodadas
while base[eixo_x][eixo_y] == "O":
    # pergunta ao user as coordenadas do barco
    pergunta_linha = int(input("Diga em qual linha está o barco: "))
    pergunta_coluna = int(input('Diga em qual coluna está o barco: '))

    if pergunta_linha == eixo_x and pergunta_coluna == eixo_y:
        print("\nParabéns, você acertou o barco!\n")
        break
    else:
        if pergunta_linha not in range(10)or pergunta_coluna not in range(10):
            print ("\nOops, escolha algo no oceano.")
        elif base[pergunta_linha][pergunta_coluna] == "X":
            print ("\nVocê já selecionou essa coordenada")
        else:
            base[pergunta_linha][pergunta_coluna] = "X"
            erros = erros + 1
            print("\nPuxa, deu água!\n")
            print("Erros = ", erros)
            print("Acertos = ", acertos, "\n")
            coluna(base)





