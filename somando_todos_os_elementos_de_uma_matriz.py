# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
-------------------------------------------------------------------------------
'''
Exercício 93 - crie uma função que calcule a soma de todos os elementos de uma 
matriz
'''
def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma

matriz = [[1, 2], [3, 4]]
print(soma_matriz(matriz))
-------------------------------------------------------------------------------
'''
Exercício 94 - Crie uma função que verifica se uma matriz é esparsa (maioria
dos elementos é igual a zero)
'''
def matriz_esparsa(matriz):
    zero_elements = 0
    size = 0
    for linha in matriz:
        zero_elements += linha.count(0)
        for coluna in linha:
            if coluna != 0:
                size += 1
    if zero_elements > size:
        return 'A matriz é esparsa'
    
    return 'A matriz não é esparsa'
matriz = [[1, 0], [2, 0], [0, 0]]
print(matriz_esparsa(matriz))
-------------------------------------------------------------------------------
'''
Exercício 96 - Crie uma função que multiplique duas matrizes m x n e n x p
'''
def produto_matriz(m, n, p):
    matriz_1 = []
    for linha in range(m):
        linha = []
        for coluna in range(n):
            linha.append(input(f'Linha{linha} Coluna{coluna}: '))
        matriz_1.append(linha[:])
    
    matriz_2 = []
    for linha in range(m):
        linha = []
        for coluna in range(n):
            linha.append(input(f'Linha{linha} Coluna{coluna}: '))
        matriz_2.append(linha[:])
        
    matriz_resultante = []
    for linha_matriz1 in range(matriz_1):
        for coluna_matriz2 in range(matriz_2[0]):
            for linha_matriz2 in range(matriz_2):
                matriz_resultante[linha_matriz1][coluna_matriz2] += matriz_1[linha_matriz1][linha_matriz2] * matriz_2[linha_matriz2][coluna_matriz2]
-------------------------------------------------------------------------------
'''
Exercício 98 - Crie uma função que determine a matriz transposta de uma matriz
'''
def matriz_transposta(n, m):
    matriz = []
    for linha in matriz:
        linha = []
        for coluna in linha:
            linha.append(input(f'Linha{linha} Coluna{coluna}: '))
        matriz.append(linha[:])
        
    matriz_tp = []
    for linha in matriz_tp:
        linha = []
-------------------------------------------------------------------------------
'''
Exercício 99
'''
def maior_menor(n, m):
    matriz = []
    maior = 0
    menor = 0
    for linha in matriz:
        linha = []
        for coluna in linha:
            element = linha.append(input(f'Linha{linha} Coluna{coluna}: '))
            if len(matriz) == 1:
                maior = menor = element
            if element > maior:
                maior = element
            if element < menor:
                menor = element
        matriz.append(linha[:])
            
        