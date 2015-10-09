# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:38:21 2015

@author: Alexandre Lima
"""

# importa o arquivo com as características dos barcos
arquivo =open("barcos.txt")

# transforma o arquivo importado em uma lista
# entretanto, ele printa com \n
linhas = arquivo.readlines()

#cria a lista com a quantidade de quadrados e os pontos dos respectivos barcos
quadrados = []
pontos = []

for l in linhas:
    # o "strip" elimina caracteres que não queremos
    limpa = l.strip()
    partes =  limpa.split()
    
    #número de quadrados por barco
    quadrados.append(int(partes[0]))
 
    #número de pontos por barco derrubado
    pontos.append(int(partes[1]))

    
    


