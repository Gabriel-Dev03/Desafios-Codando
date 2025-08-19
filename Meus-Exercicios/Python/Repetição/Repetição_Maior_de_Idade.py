print("-="*30)

print("Ano de nascimento")

for c in range(1 , 8):
    nome = input(f"Digite o nome da {c}ª pessoa: ")
    ano = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    if 2025 - ano < 18:
        print(f"{nome} é menor de idade.")
    else:
        print(f"{nome} é maior de idade.")
print("-="*30)