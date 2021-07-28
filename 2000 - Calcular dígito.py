def calcular_digito(chave):
    splitada = chave.split('.')
    splitada[len(splitada)-1] = splitada[len(splitada)-1].split('-')[0]
    soma = 0
    for i in splitada:
        lista = '-'.join(i).split('-')
        lista = [int(i) for i in lista]
        soma+=max(lista)
    digito = soma%10
    digito = str(digito)
    return digito

def ehValido(digito, chave):
    return "VALIDO" if digito == chave else "INVALIDO"

chave = input()
while(chave!="FIM"):
    digito = calcular_digito(chave)
    validadeDigito = ehValido(digito, chave[:-2:-1])
    print(validadeDigito)
    chave = input()
