def ClassificaAluno(media, faltas):
    if faltas <= 10 and media >= 9.5: return "APROVADO COM LOUVOR"
    elif faltas <=10 and media >= 7: return "APROVADO"
    elif faltas > 10: return "REPROVADO POR FALTAS"
    return "REPROVADO"


media, qtdFaltas = float(input()), int(input())
print(ClassificaAluno(media, qtdFaltas))
