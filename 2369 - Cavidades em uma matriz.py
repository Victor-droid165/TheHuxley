def getRedor(i, j, linhas, colunas):
    redor = []
    for k in range(-1, 2):
        for z in range(-1, 2):
            try:
                if(not(i+k == i and j+z == j)):
                    if(not(i+k < 0 or i+k >= linhas)):
                        if(not(j+z < 0 or j+k >= colunas)):
                            matriz[i+k][j+z]
                            redor.append((i+k, j+z))
            except:
                pass
    return redor

def preencheConjuntoComMenorValorRedor(matriz, linhas, colunas):
    d = dict()
    conjunto = set()
    for i in range(linhas):
        for j in range(colunas):
            menor_valor_redor = (i, j)
            redor = getRedor(i, j, linhas, colunas)
            for linha, coluna in redor:
                if(matriz[linha][coluna] <= matriz[menor_valor_redor[0]][menor_valor_redor[1]]):
                    menor_valor_redor = (linha, coluna)
                else:
                    d[f"{linha}{coluna}"] = 1
            conjunto.add(menor_valor_redor)
    return conjunto, d

def removeElementosConjuntoComRedorRedundante(d, conjunto):
    for elemento in d.keys():
        x,y = elemento[0], elemento[1]
        tupla = (int(x),int(y))
        if(tupla in conjunto):
            try:
                conjunto.remove(tupla)
            except:
                pass
    return conjunto

linhas = int(input())
colunas = int(input())

matriz = [[int(input()) for coluna in range(colunas)] for linha in range(linhas)]
conjunto, d = preencheConjuntoComMenorValorRedor(matriz, linhas, colunas)
conjunto = removeElementosConjuntoComRedorRedundante(d, conjunto)
matriz = list(conjunto)
matriz.sort()
print(matriz)