pi = 3.14
r1, r2 = float(input()), float(input())
a1, a2 = pi*r1**2, pi*r2**2
classificacao = "Iguais" if a1 == a2 else ("Primeiro circulo" if a1>a2 else "Segundo circulo")
print(classificacao)
