print("-="*30)
aumento = 0
salario = float(input("Digite o seu salario: "))
if salario <= 1250:
    aumento = salario * 1.15
else:
    aumento = salario * 1.10

print(f"O seu salário com aumento é R${aumento:.2f}.")
print("-="*30)
