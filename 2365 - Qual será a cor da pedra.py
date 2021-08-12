# Para saber a cor da pedra nessa célula, é preciso saber a cor das pedras
# nas três células {(i, j − 1), (i − 1, j − 1), (i − 1, j)}.
def contaPedrasNas3Posicoes(matriz, i, j):
    contPedraBranca = 0
    contPedraPreta = 0
    #checa as três células
    for z in range(2):
        for k in range(2):
            if(z == k and z == 0): continue
            if(matriz[j-z][i-k]):
                contPedraPreta+=1
            else:
                contPedraBranca+=1
    return(contPedraPreta,contPedraBranca)

# Será preta (1) se as 3 posições tiverem uma maior quantidade de pedras brancas
# Será branca (0) se as 3 posições tiverem uma maior quantidade de pedras pretas
def preencheMatrizComPedras(matriz, ordem):
    for i in range(1,ordem):
        for j in range(1,ordem):
            contPedraPreta, contPedraBranca = contaPedrasNas3Posicoes(matriz, i, j)
            if(contPedraPreta > contPedraBranca):
                matriz[i][j] = 0
            else:
                matriz[i][j] = 1
    return matriz

ordem = int(input())
matriz = [[int(coluna) for coluna in input().split()] for linha in range(ordem)]
preencheMatrizComPedras(matriz,ordem)

print(matriz[ordem-1][ordem-1])
