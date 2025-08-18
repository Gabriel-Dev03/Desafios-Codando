print("="*30)

nome = input("Digite seu nome completo: ")

print(f"O nome completo tem {len(nome.strip())} caracteres ")
print(f"O nome completo todo minúsculo ficaria {nome.lower()} ")
print(f"O nome completo todo maiúsculo ficaria {nome.upper()} ")

nome = nome.split()

print(f"O primeiro nome tem {len(nome[0])} caracteres ")

print("="*30)