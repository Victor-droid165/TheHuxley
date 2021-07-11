def verificaTamLista(tam):
    return tam <= 0

def preencheLista(tam, lista):
    for i in range(tam):
        lista.append(int(input()))
    return lista

tamLista = int(input())
if verificaTamLista(tamLista):
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    lista = preencheLista(tamLista, [])
    tamLista2 = int(input())

    if verificaTamLista(tamLista2):
        print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        lista2 = preencheLista(tamLista2, [])
        listaUniao = lista+lista2
        
        listaUniaoString = str(listaUniao)
        print(listaUniaoString[1:len(listaUniaoString)-1].replace(", ", " "))
