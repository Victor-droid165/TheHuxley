contn = False
while True:
    lista = []
    for i in range(1000):
        if contn == True:
            x = int(input())
            if x == -1:
                exit()
        else:
            x = int(input())
            contn = False
        lista.append(x)
    n = int(input())
    contn = True
    print(f"{n} appeared {lista.count(n)} times")
