def listaToString(lista):
    if(len(lista) == 0): return "[ ]"
    listaString = str(lista)
    n = len(str(lista))
    listaString = listaString[1:n-1]
    listaString = "[ " + listaString.replace(", ", " ") + " ]"
    return listaString

def myInsert(lista, pos, valor):
    tam = len(lista)
    if(pos>tam): raise IndexError("A posicao 1 estah fora do intervalo")
    if(not pos): return [valor] + lista
    if(pos == tam): return lista + [valor]
    return lista[:pos] + [valor] + lista[pos:]

n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
posicao = int(input())
valorASerColocado = int(input())

listaString = listaToString(lista)
print(listaString)

try:
    lista2 = myInsert(lista, posicao, valorASerColocado)
    lista2String = listaToString(lista2)
    print(lista2String)
except IndexError as e:
    print(e)
