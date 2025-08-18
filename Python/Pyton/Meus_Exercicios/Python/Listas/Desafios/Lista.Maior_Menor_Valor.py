numeros = [10, 5, 8, 20, 3]
maior = numeros[0]
menor = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print("Maior:", maior, "Menor:", menor)
