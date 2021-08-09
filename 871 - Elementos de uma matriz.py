#Declaração de funções e procedimento

def getValoresNegativosNaMatriz(matriz):
    valoresNegativos = []
    for linha in matriz:
        for elemento in linha:
            if elemento < 0: valoresNegativos.append(elemento)
    return valoresNegativos

def getValoresPositivosNaMatriz(matriz):
    valoresPositivos = []
    for linha in matriz:
        for elemento in linha:
            if elemento > 0: valoresPositivos.append(elemento)
    return valoresPositivos

def printaMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j]) if matriz[i][j]==matriz[i][colunas-1] else print(matriz[i][j], end=" ")

def calculoDiagonais(linhas, colunas):
    return linhas == colunas

def calculaDiagonais(matriz):
    diagonalPrincipal, diagonalSecundaria = 0,0
    cont = len(matriz)-1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if(i==j):
                diagonalPrincipal+=matriz[i][j]
            if(j==cont):
                cont-=1
                diagonalSecundaria+=matriz[i][j]
    return diagonalPrincipal, diagonalSecundaria

#Declaração de variáveis

linhas, colunas = [int(i) for i in input().split()]
matriz = [[int(input()) for i in range(colunas)] for i in range(linhas)]
valoresPositivos = getValoresPositivosNaMatriz(matriz)
valoresNegativos = getValoresNegativosNaMatriz(matriz)

print("Matriz formada:")
printaMatriz(matriz)
        
if(calculoDiagonais(linhas,colunas)):
    diagonalPrincipal, diagonalSecundaria = calculaDiagonais(matriz)
    print(f"A diagonal principal e secundaria tem valor(es) {diagonalPrincipal} e {diagonalSecundaria} respectivamente.")
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")
    
print(f'''A matriz possui {len(valoresNegativos)} numero(s) menor(es) que zero.
A matriz possui {len(valoresPositivos)} numero(s) maior(es) que zero.''')
