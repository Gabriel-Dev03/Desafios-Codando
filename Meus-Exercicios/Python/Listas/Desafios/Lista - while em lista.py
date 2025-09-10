print("-=" * 30)

numeros = []

while True:
    num = int(input("Digite um número: ( -1 para parar ) "))
    
    if num == -1:
        break

    if num not in numeros:
        numeros.append(num)
        print("Número adicionado com sucesso...")
    else:
        print("Número duplicado! Não vou adicionar...")

      
        while True:
            continuar = input("Quer continuar? [S/N] ").strip().upper()
            if continuar in ("S", "N"):
                break
            print("Resposta inválida! Digite apenas S ou N.")
        
        if continuar == "N":
            break

print(f"\nVocê digitou os valores {sorted(numeros)}")
