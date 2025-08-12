valores = [10, 45, 2, 99, 23]
maior = valores[0]

for v in valores:
    if v > maior:
        maior = v

print(f"O maior valor é {maior}")
