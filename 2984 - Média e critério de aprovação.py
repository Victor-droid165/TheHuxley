n1,n2,n3,f = float(input()), float(input()), float(input()), float(input())
p1, p2, p3 = 2, 2, 3
media = round((n1*p1+n2*p2+n3*p3)/ (p1+p2+p3), 1)

if f < 0.75: msg = ("Aluno reprovado por faltas!" )
elif media > 9: msg = "Aluno aprovado com louvor!"
elif media >= 6: msg = "Aluno aprovado!"
elif media>=4: msg = "Aluno de rec!"
else: msg = "Aluno reprovado!"
print(f'''Frequencia: {int(f*100)}%
Media: {media:.1f}
{msg}''')
