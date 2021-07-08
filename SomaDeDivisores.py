cont = 5
somasDivisoresNum = {}
arraySomas=[]
while(cont):
    num = int(input())
    soma = 0
    for i in range(1,num+1):
        if(num%i == 0):
            soma += i
    arraySomas.append(soma)
    somasDivisoresNum[soma] = num
    cont-=1
print(somasDivisoresNum[max(arraySomas)])
