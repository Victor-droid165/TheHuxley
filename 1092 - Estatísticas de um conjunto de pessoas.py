dic={}
for i in range(10):
    salario, sexo = float(input()), input()
    if sexo not in dic:
        dic[sexo] = []
    dic[sexo].append(salario)
qtdHomens = len(dic['m'])
qtdMulheres = len(dic['f'])
print(qtdHomens)
print(qtdMulheres)
print("%.1f" % ((sum(dic['m']) + sum(dic['f']))/(qtdHomens+qtdMulheres)))
print("m" if max(dic['m']) > max(dic['f']) else "f")
print("%.1f" % (sum(dic['m'])/qtdHomens))
