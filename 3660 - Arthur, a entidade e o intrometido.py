def getSomaLinhasPares(matriz, ordem):
    soma = 0
    for i in range(0, ordem, 2):
        for j in range(ordem):
            soma+= matriz[i][j]
    return soma

def getSomaColunasImpares(matriz, ordem):
    soma = 0
    for i in range(ordem):
        for j in range(1,ordem, 2):
            soma+= matriz[i][j]
    return soma

def getSomaDiagonalPrincipal(matriz, ordem):
    soma = 0
    for i in range(ordem):
        for j in range(ordem):
            if i==j:
                soma+= matriz[i][j]
    return soma

def getPontuacaoVencedora(pontuacoes):
    maior_pontuacao = 0
    for i in range(len(pontuacoes)):
        if pontuacoes[i] > maior_pontuacao:
            maior_pontuacao = pontuacoes[i]
    return maior_pontuacao

def houveVencedor(pontuacoes):
    maior_pontuacao = getPontuacaoVencedora(pontuacoes)
    for i in range(len(pontuacoes)-1):
        if pontuacoes[i] == pontuacoes[i+1] and pontuacoes[i]==maior_pontuacao:
            return False
    return True

def getVencedor(jogadores):
    maior_pontuacao = getPontuacaoVencedora(list(jogadores.values()))
    for jogador,pontuacao in jogadores.items():
        if pontuacao == maior_pontuacao:
            vencedor = jogador
            return vencedor

ordem = int(input())
matriz = [[int(coluna) for coluna in input().split()] for linha in range(ordem)]
jogadores = {
    "Arthur":getSomaLinhasPares(matriz, ordem),
    "entidade":getSomaColunasImpares(matriz, ordem),
    "intrometido":getSomaDiagonalPrincipal(matriz, ordem)
    }
pontuacoes_lista = list(jogadores.values())
if houveVencedor(pontuacoes_lista):
   vencedor = getVencedor(jogadores)
   artigo = "A " if vencedor == "entidade" else("O " if vencedor == "intrometido" else "")
   print(f"{artigo}{vencedor} venceu!\nResultado: {jogadores[vencedor]}")
else:
    print("Empate!")
    maior_pontuacao = max(pontuacoes_lista)
    print(f"Resultado: {maior_pontuacao}")
