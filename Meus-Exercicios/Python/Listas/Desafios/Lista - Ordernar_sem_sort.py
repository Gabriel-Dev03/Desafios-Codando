print("-=" * 30)

numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f"Adicionado na posição {pos} da lista...")
                break
            pos += 1