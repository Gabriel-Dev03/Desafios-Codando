print("-=" * 30)

numeros = []
pares = []
impares = []
while True:
    num =int(input("Digite um número: (ou -1 pra parar "))
    if num == -1:
        break
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f"\nA lista completa é {numeros}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")

print("-=" * 30)