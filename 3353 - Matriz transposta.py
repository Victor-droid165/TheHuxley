linhas, colunas = [int(i) for i in input().split()]
matriz = [[int(i) for i in input().split()] for i in range(linhas)]
transposta = [[linha[i] for linha in matriz] for i in range(colunas)]
for i in transposta:
    for j in i:
        print(j, end=" ")
    print()
