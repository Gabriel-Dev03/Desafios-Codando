print("-=" * 30)

numeros = []
maior = menor = 0
posicao_maior = posicao_menor = 0

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

    if i == 0: 
        maior = menor = num
        posicao_maior = posicao_menor = i
    else:
        if num > maior:
            maior = num
            posicao_maior = i
        if num < menor:
            menor = num
            posicao_menor = i

print(f"\nOs números digitados foram: {numeros}")
print(f"O maior valor digitado foi {maior} na posição {posicao_maior}")
print(f"O menor valor digitado foi {menor} na posição {posicao_menor}")

print("-=" * 30)