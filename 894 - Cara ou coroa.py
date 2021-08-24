combinacoes = []

def getCombinacoes(numero, D, atual=""):
    if(numero > 0):
        numero-=1
        for i in ("C", "K"):
            atual += i
            atual = getCombinacoes(numero, D, atual)
            combinacao = atual+i
            if numero == 0:
                qtdCara = combinacao.count("C")
                qtdCoroa = combinacao.count("K")
                if(abs(qtdCara - qtdCoroa) == D):
                    combinacoes.append(combinacao)
    return atual[:-1]

N,D = [int(i) for i in input().split()]
getCombinacoes(N,D)
print(len(combinacoes))
