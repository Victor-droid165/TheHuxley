largura, comprimento, altura = float(input()), float(input()), float(input())
msg = ("Permitida" if largura <= 45 and comprimento <= 56 and altura <= 25 else "Proibida").upper()
print(msg)
