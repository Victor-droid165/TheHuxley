N = int(input()) #linhas
M = int(input()) #colunas
matriz = []
T = 0
D = 0

for i in range(N):
    matriz.append([])
    cont = M-i-1
    for j in range(M):
        matriz[i].append(int(input()))
        if M == N:
            if(i == j): T += matriz[i][j]
            if(j == cont): D += matriz[i][j]
            
msg = "A matriz nao possui traco" if M!=N else f"{T}\n{D}"    
print(msg)
for i in range(N):
    for j in range(M):
        print(matriz[i][j], end=" ") if j != M-1 else print(matriz[i][j])
