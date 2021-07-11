N = int(input())
coposQuebrados = 0
for i in range(N):
    lista = [int(i) for i in input().split()]
    if lista[0] > lista[1]: coposQuebrados+=lista[1]
print(coposQuebrados)
