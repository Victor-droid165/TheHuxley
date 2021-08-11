def printaMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
        
def multiplicaDiagonalPrincipal(matriz, linhas, colunas, k):
    matriz = [[(matriz[linha][coluna]*k if coluna==linha else matriz[linha][coluna]) for coluna in range(colunas)] for linha in range(linhas)]
    return matriz

linhas, colunas = 4,4
k = int(input())
while(k):
    #recebe a matriz com as colunas no lugar das linhas
    matriz = [[int(input()) for coluna in range(colunas)] for linha in range(linhas)]
    #recebe a matriz transposta para ficar de conformidade com a questão
    matriz = [[linha[coluna] for linha in matriz] for coluna in range(colunas)]
    matriz = multiplicaDiagonalPrincipal(matriz, linhas, colunas, k)
    printaMatriz(matriz)
    k = int(input())
