print("-= "*30)

nome = input("Digite o seu nome completo: ").strip().capitalize()
print(f"Seu nome digitado foi {nome} ")

print(f"O seu primeiro nome é {nome.split()[0]}") 
print(f"O seu ultimo nome é {nome.split()[-1]}")

print("-= "*30)