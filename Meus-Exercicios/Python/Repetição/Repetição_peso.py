print("-="*30)

print("Maior e Menor Peso")

for c in range(1, 6):
    nome = input(f"Digite o nome da {c}ª pessoa: ")
    peso = float(input(f"Digite o peso da {c}ª pessoa: "))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é {maior} kg")
print(f"O menor peso é {menor} kg")
print("-="*30)
