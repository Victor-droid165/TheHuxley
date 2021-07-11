n = int(input())
lista = []
for i in range(n):
    x = int(input())
    lista.append(x)
posicao = int(input())
if len(lista) == 0:
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elementos")
elif posicao > len(lista)-1:
    print("[",end=' ')
    for k in range(len(lista)):
        print(f'''{lista[k]}''',end=' ')
    print("]")
    print("Nao eh possivel remover o elemento")
else:
    numero = lista[posicao]
    for j in range(len(lista)):
        if lista[j] == numero:
            index = j
            break
    if index == 0 or index == -1*len(lista):
        poscerta = lista[index+1:]
    elif index == len(lista)-1 or index == -1:
        poscerta = lista[:index:]
    else:
        poscerta = lista[0:index] + lista[index+1:]
    print("[",end=' ')
    for g in range(len(lista)):
        print(f'''{lista[g]}''',end=' ')
    print("]")
    print(f'''O item {numero} serah removido da lista''')
    print("[",end=' ')
    for z in range(len(poscerta)):
        print(f'''{poscerta[z]}''',end=' ')
    print("]")
