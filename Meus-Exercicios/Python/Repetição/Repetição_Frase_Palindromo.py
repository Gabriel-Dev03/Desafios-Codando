print("-="*30)

print("Frase Palíndromo")

frase = str(input("Digite uma frase: ")).strip().upper()

for c in frase:
    if c == " ":
        frase = frase.replace(c, "")
if frase == frase[::-1]:
    print("A frase digitada é um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
print("-="*30)