qtdPrincesas = int(input())
qtdEleitores = int(input())
matriz = [[int(coluna) for coluna in input().split()] for linha in range(qtdEleitores)]

#A soma da coluna n será a quantidade de votos da n-ésima princesa
#Basta pegar a matriz transposta e somar cada linha para obter o resultado desejado

transposta = [[matriz[coluna][linha] for coluna in range(qtdEleitores)] for linha in range(qtdPrincesas)]

cont = 0
for linha in transposta:
    cont+=1
    print(f"Princesa {cont}: {sum(linha)} voto(s)")
