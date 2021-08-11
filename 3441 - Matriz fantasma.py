def newMatrizQuadrada(ordem):
    matriz = []
    for i in range(n):
        matriz.append([0]*n)
    return matriz

def getMatrizFantasma(matriz, linhas, colunas):
    cont = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if(coluna>=cont):
                matriz[linha][coluna] = coluna+1
        cont+=1
    return matriz

def printaMatrizFantasma(matriz):
    for vetor in matriz:
        for elemento in vetor:
            if elemento!=0:
                print(elemento, end=" ") if elemento!=n else print(elemento)
            else:
                print(end="  ")

n = int(input())
matriz = newMatrizQuadrada(n)
matriz = getMatrizFantasma(matriz, n, n)
printaMatrizFantasma(matriz)
