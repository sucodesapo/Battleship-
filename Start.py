# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:50:46 2015

@author: Alexandre Lima
"""

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
