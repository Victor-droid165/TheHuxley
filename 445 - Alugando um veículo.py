dias = int(input())
diaria = 90
maxKm = 100*dias
kmTotal = int(input())
gasto = (kmTotal-maxKm)*12+diaria*dias if kmTotal>maxKm else diaria*dias
print(f"{gasto:.2f}")
