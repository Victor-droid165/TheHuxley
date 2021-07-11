def myPop(lista, pos):
    tam = len(lista)
    if tam == 0: raise IndexError("A lista estah vazia - nao eh possivel remover elementos")
    elif pos > tam-1: raise IndexError("Nao eh possivel remover o elemento")
    else:
        numero = lista[pos]
        if pos == 0 or pos == -1*tam: poscerta = lista[pos+1:]
        elif pos == tam-1 or pos == -1: poscerta = lista[:pos:]
        else: poscerta = lista[0:pos] + lista[pos+1:]
        return poscerta, numero

def listaToString(lista):
    if(len(lista) == 0): return "[ ]"
    listaString = str(lista)
    n = len(str(lista))
    listaString = listaString[1:n-1]
    listaString = "[ " + listaString.replace(", ", " ") + " ]"
    return listaString

n = int(input())
lista = []
for i in range(n):
    x = int(input())
    lista.append(x)
posicao = int(input())

listaString = listaToString(lista)
print(listaString)
try:
    listaValorRemovido, valorRemovido = myPop(lista, posicao)
    print(f'''O item {valorRemovido} serah removido da lista''')
    lista2String = listaToString(listaValorRemovido)
    print(lista2String)
except IndexError as e:
    print(e)
