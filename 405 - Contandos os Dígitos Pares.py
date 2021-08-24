cont = 0

def ContaDigitosPares(numero):
    global cont
    if numero != "":
        if int(numero[0])%2 == 0: cont+=1
        ContaDigitosPares(numero[1:])

num = input()
ContaDigitosPares(num)
print(cont)
