numeros = [4, 1, 3, 5, 2]
ordenada = []
while numeros:
    menor = numeros[0]
    for n in numeros:
        if n < menor:
            menor = n
    ordenada.append(menor)
    numeros.remove(menor)
print(ordenada)
