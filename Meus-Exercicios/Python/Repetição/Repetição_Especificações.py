print("-="*30)

print("Dados das pessoas")
media_idade = 0
homem_mais_velho = ""
mulheres_menos_20 = 0
for c in range(1, 5):
    nome = input(f"Nome da {c}ª pessoa: ")
    idade = int(input(f"Idade da {c}ª pessoa: ")) 
    sexo = input(f"Sexo da {c}ª pessoa (M/F): ").strip().upper()
    media_idade += idade
    if sexo == "M":
        if c == 1:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
        else:
            if idade > idade_homem_mais_velho:
                homem_mais_velho = nome
                idade_homem_mais_velho = idade
    if sexo == "F" and idade < 20:
        print(f"{nome} é uma mulher com menos de 20 anos.")
        mulheres_menos_20 += 1
print(f"Temos {mulheres_menos_20} mulheres com menos de 20 anos.")
print(f"A média de idade do grupo é de {media_idade/4:.1f} anos.")
print(f"O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.")
print("-="*30)
