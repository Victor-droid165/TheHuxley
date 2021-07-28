cidade = input().upper()
array = ["",None,None]

while(cidade != "FIM"):
    km = int(input())
    passagem = float(input())
    passagem *= 2
    if(array[1] is None):
        if(passagem <= 300):
            array[1] = km
            array[2] = passagem
            array[0] = cidade
    elif(passagem <= 300 and array[1] < km):
            array[1] = km
            array[2] = passagem
            array[0] = cidade
    cidade = input().upper()

if(array[0] == ""):
    print("SEM DESTINO")
else:
    print(array[0])

'''
Python 3.8+
array = ["",None,None]
while((cidade := input().upper()) != "FIM"):
    km, passagem= int(input()),float(input())*2
    if(array[1] is None and passagem <= 300): array[1],array[2],array[0]= km,passagem,cidade
    elif(passagem <= 300 and array[1] < km): array[1],array[2],array[0]= km,passagem,cidade
print("SEM DESTINO") if(array[0] == "") else print(array[0])'''
