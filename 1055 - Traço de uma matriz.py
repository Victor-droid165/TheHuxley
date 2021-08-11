def getDiagonalPrincipal(matriz, linhas, colunas):
    for linha in range(linhas):
        for coluna in range(colunas):
            if linha == coluna:
                yield matriz[linha][coluna] 

ordem = int(input())
matriz = [[float(coluna) for coluna in input().split()] for linha in range(ordem)]
diagonalPrincipal = getDiagonalPrincipal(matriz, ordem, ordem)
diagonalPrincipal = list(diagonalPrincipal)
resposta = "tr(A) = "
for i in diagonalPrincipal:
    resposta+= f"({i:.2f}) + "
resposta += f"= {sum(diagonalPrincipal):.2f}"
print(resposta[::-1].replace("+ ", "", 1)[::-1])
