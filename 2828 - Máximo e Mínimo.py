n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
print(f'''Maior: {max(lista)} apareceu {lista.count(max(lista))} vezes
Menor: {min(lista)} apareceu {lista.count(min(lista))} vezes''')
