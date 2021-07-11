n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
deslocamentos = int(input())
for i in range(deslocamentos,n):
    print(lista[i])
for i in range(deslocamentos):
    print(lista[i])
