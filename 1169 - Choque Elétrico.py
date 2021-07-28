level = int(input())
lista=["20+level**3", "8000+(level-10)**2", "9000+5*level", "9300+2*level", "9500+level"]
minimo, maximo = 1, 20
tam = len(lista)
dic = {}

for i in range(len(lista)):
    dic[range(minimo, maximo+1)] = lista[i]
    minimo += 20
    maximo += 20

for i in dic.keys():
    if level in i:
        print(f"Potencia de : {eval(dic[i])} W")
        break
