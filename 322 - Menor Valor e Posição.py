n = int(input())
valores = input().split()
for i in range(len(valores)):
    valores[i] = int(valores[i])
print(f"Menor valor: {min(valores)}\nPosicao: {valores.index(min(valores))}")
