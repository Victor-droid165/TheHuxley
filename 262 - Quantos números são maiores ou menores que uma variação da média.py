n = int(input())
lista = []
for i in range(n):
    x = float(input())
    lista.append(x)
media = sum(lista)/n
print(f"{media:.2f}")
conts = 0
contn = 0
for j in range(len(lista)):
    if lista[j] > media + 0.1*media:
        conts+=1
    elif lista[j] < media - 0.1*media:
        contn +=1
print(f"{conts}\n{contn}")
