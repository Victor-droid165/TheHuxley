arrecadacoes = []
arrecadacao = float(input())
while(arrecadacao>=0):
    arrecadacoes.append(arrecadacao)
    arrecadacao = float(input())
total = sum(arrecadacoes)
qtdArrecadacoes = len(arrecadacoes)
if(not qtdArrecadacoes):
    qtdArrecadacoes = 1
media = total/qtdArrecadacoes
print('''Insira os valores das doacoes:
Total arrecadado: %.2f
Valor medio da doacao: %.2f''' % (total, media))
