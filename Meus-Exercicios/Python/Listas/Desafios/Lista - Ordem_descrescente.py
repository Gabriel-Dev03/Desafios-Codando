print("-=" * 30)

numeros = []

while True:
    num = int(input("Digite um número (ou -1 para parar): "))
    if num == -1:
        break
    numeros.append(num)

print(f"Os números em ordem decrescente são: {sorted(numeros, reverse=True)}")
print(f"Você digitou {len(numeros)} números ao todo.")
if 5 in numeros:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não foi encontrado na lista.")

print("-=" * 30)