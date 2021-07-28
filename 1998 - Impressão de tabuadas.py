def maiorAB(a,b):
    return a>b

def checaIntervalo(num):
    return 1<=num<=9

num, numLimite = int(input()), -1
while( (not checaIntervalo(num)) or (not checaIntervalo(numLimite))):
    if(not checaIntervalo(num)):
        print("Insira um número inicial entre 1 e 9")
        num = int(input())
        continue
    numLimite = int(input())
    if(not checaIntervalo(numLimite)): print("Insira um número final entre 1 e 9")
        
if(maiorAB(num,numLimite)): print("Nenhuma tabuada nesse intervalo")
else:
    for i in range(num,numLimite+1):
        for j in range(1,10):
            print(f"{i} x {j} = {i*j}")
        if i != numLimite: print()
