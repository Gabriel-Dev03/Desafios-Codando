print("-="*30)  

print("Contagem de 1 a 500")
impares = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        impares += c
print(f"A soma dos números ímpares de 1 a 500 que são múltiplos de 3 é: {impares}")
print("-="*30)