ordem = int(input())
matriz = [[(int(j) if int(j) > 0 else int(j)*2 ) for j in input().split()] for i in range(ordem)]
modificada = [elemento for elemento in zip(*matriz)]
for elemento in modificada:
    print(*i)
