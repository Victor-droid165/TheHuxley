def existeVizinho(indice, valor):
    return (indice!=valor)

def getQuantidadeVizinhosPossiveis(linha, coluna, ordem, valores):
    cont=0
    direcao= {
        "posicaoVertical":[],
        "posicaoHorizontal":[]
    }
    vertical = False
    for k in [linha,coluna]:
        vertical = not vertical
        for z in range(len(valores)):
            if(vertical and existeVizinho(k, valores[z])):
                cont+=1
                direcao["posicaoVertical"].append(1)
            elif((not vertical) and existeVizinho(k, valores[z])):
                cont+=1
                direcao["posicaoHorizontal"].append(1)
            elif(vertical):
                direcao["posicaoVertical"].append(0)
            else:
                direcao["posicaoHorizontal"].append(0)
                
    return cont, direcao


def getVizinhosValidos(matriz, i, j, ordem):
    vizinhosValidos = []
    valores=[0, ordem-1]
    qtdVizinhosValidos, direcao = getQuantidadeVizinhosPossiveis(i, j, ordem, valores)
    posicao = "Vertical"
    cont = -1
    while(len(direcao["posicao"+posicao]) > 0):
        if(direcao["posicao"+posicao].pop(0)):
            elemento = matriz[i+cont][j]
            if(elemento > 0):
                vizinhosValidos.append(elemento)
        cont *= -1
    posicao = "Horizontal"
    cont = -1
    while(len(direcao["posicao"+posicao]) > 0):
        if(direcao["posicao"+posicao].pop(0)):
            elemento = matriz[i][j+cont]
            if(elemento > 0):
                vizinhosValidos.append(elemento)
        cont *= -1
    return vizinhosValidos


ordem = int(input())
matriz = [[int(coluna) for coluna in input().split()] for linha in range(ordem)]
somaVizinhosValidos = 0
qtdVizinhosValidos = 0
for i in range(ordem):
    for j in range(ordem):
        vizinhos = getVizinhosValidos(matriz,i,j,ordem)
        qtdVizinhosValidos += len(vizinhos)
        somaVizinhosValidos += sum(vizinhos)
print(qtdVizinhosValidos)
print(somaVizinhosValidos)