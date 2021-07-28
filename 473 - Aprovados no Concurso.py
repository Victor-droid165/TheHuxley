def passou(port, mat, redacao):
    if(port/50 >= 0.8):
        if(mat/35 >= 0.6):
            if(redacao >= 7):
                return True
    return False
    
port = int(input())
qtdAprovados = 0
while(port>=0):
    mat = int(input())
    redacao = float(input())
    if(passou(port, mat, redacao)):
        qtdAprovados+=1
    port = int(input())
print(qtdAprovados)
