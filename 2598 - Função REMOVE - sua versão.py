def myRemove(lista, valor):
    tam = len(lista)
    encontrado = False
    indice = -1
    if(not tam):
        raise ValueError("A lista estah vazia - nao eh possivel remover elemento")
    for i in range(tam):
        if(lista[i] == valor):
            encontrado = True
            indice = i
            break
    if(encontrado):
        if(indice+1 < tam):
            lista = lista[:indice] + lista[indice+1:]
        else:
            lista = lista[:indice] + lista[indice+1:]
        return lista
    else:
        raise ValueError(f"Nao eh possivel remover o elemento {valor}")

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
    lista.append(int(input()))
valorASerRemovido = int(input())

listaString = listaToString(lista)
try:
    listaValorRemovido = myRemove(lista, valorASerRemovido)
    lista2String = listaToString(listaValorRemovido)
    print(listaString)
    print(lista2String)
except ValueError as e:
    print(listaString.replace("  ", " "))
    print(e)
