lista = []
for i in range(3):
    x = int(input())
    lista.append(x)
for i in lista:
    if (i != max(lista) and i != min(lista)):
        print(i)
