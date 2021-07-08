qtdPessoas = int(input())
cidade = input().lower()
qtdQuartos = int(input())
dic = {
    "pipa":{2:600, 3:900, "gastosPessoa":75},
    "fortaleza":{3:950, 4:1120, "gastosPessoa":60}
    }
total = dic[cidade][qtdQuartos] + dic[cidade]["gastosPessoa"]*qtdPessoas
print("%.2f\n%.2f" % (total, total/qtdPessoas))
