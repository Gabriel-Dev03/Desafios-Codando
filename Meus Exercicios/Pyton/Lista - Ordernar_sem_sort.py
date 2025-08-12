valores = [4, 2, 9, 1, 5]
for i in range(len(valores)):
    for j in range(i+1, len(valores)):
        if valores[i] > valores[j]:
            valores[i], valores[j] = valores[j], valores[i]

print("Lista ordenada:", valores)
