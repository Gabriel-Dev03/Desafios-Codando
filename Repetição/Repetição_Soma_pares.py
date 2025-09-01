print("-="*30)
soma = 0
print("Soma dos Números Pares")

for c in range(0, 6):
    num = int(input(f"Digite um número: "))
    if num % 2 == 0:
        soma += num
    else:
        print(f"{num} não é par, não será somado.")
print(f"A soma dos números pares é: {soma}")

print("-="*30)
