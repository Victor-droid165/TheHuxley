lista = [(1 if input()=="True" else 0) for i in range(5)]
soma = sum(lista)
classificacao = "Assassino" if soma == 5 else ("Cumplice" if soma >=3 else("Suspeita" if soma ==2 else "Inocente"))

print(f'''Telefonou para a vitima?
Esteve no local do crime?
Mora perto da vitima?
Devia para a vitima?
Ja trabalhou com a vitima?
{classificacao}''')
