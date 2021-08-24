ordem = int(input())
matriz = []
cont = 1

for i in range(ordem):
    matriz.append([])
    for j in range(ordem):
        matriz[i].append(cont)
        cont+=1
            
listaMsg = ["Matriz:"]
espacamento = " "*2

for i in range(ordem):
    listaMsg.append("")
    for j in range(ordem):
        listaMsg[-1] += f"{espacamento}{matriz[i][j]}"

listaMsg.append("")
listaMsg.append("Diagonal Principal:")

for i in range(ordem):
    listaMsg.append("")
    espacamento = " "*2
    for j in range(ordem):
        if(i == j):
            listaMsg[-1] += f"{espacamento}{matriz[i][j]}"
            break
        espacamento += " "*3

listaMsg.append("")
listaMsg.append("Diagonal Secundaria:")

for i in range(ordem):
    listaMsg.append("")
    espacamento = " "*2
    cont = ordem-i-1
    for j in range(ordem):
        if(j == cont):
            listaMsg[-1] += f"{espacamento}{matriz[i][j]}"
            break
        espacamento += " "*3
        
print(*listaMsg, sep='\n')
