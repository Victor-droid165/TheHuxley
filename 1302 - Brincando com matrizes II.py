ordem = 3
matriz = [[int(input()) for j in range(ordem)]for i in range(ordem)]
positivos, menores, soma = [], [], 0

for i in range (len(matriz)):
    menores.append(min(matriz[i]))
    for j in range(len(matriz[i])):
        if(matriz[i][j]>0): positivos.append(matriz[i][j])
        if(i != j): soma+= matriz[i][j]
        
mediaPositivos = sum(positivos)/len(positivos)
menorValor = min(menores)
delta = 1 if menorValor%2==0 else 0
print(f"{mediaPositivos:.2f} {menorValor} {delta} {soma}")
