n = int(input())
if n == 0:
    print("Numero de notas invalido.")
else:
    notas = []
    for i in range(n):
        nota = float(input())
        notas.append(nota)
    soma = 0
    for j in range(len(notas)):
        print(f"Nota {j+1}: {notas[j]}")
        soma+=notas[j]
    print(f"Media: {soma/n:.2f}" )
