n = int(input())
if n==0: print("Lista vazia - O valor de S eh zero")
elif n<0: print("O valor informado para N foi negativo")
else:
    lista = []
    S = 0
    for i in range(n):
        lista.append(int(input()))
    for i in range(int(n/2)):
        S += (lista[i] - lista[(i+1)*(-1)])**2
    if(n%2):
        S += (lista[int(n/2)])**2
    print(f"S = {S}")
