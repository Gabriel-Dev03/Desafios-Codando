print("-="*30)

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))
print(f"Você digitou os números {n1}, {n2} e {n3}.")

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número.")    
elif n3 > n1 and n3 > n2:
    print(f"{n3} é o maior número.")
elif n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número.")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor número.")
elif n3 < n1 and n3 < n2:
    print(f"{n3} é o menor número.")
else:
    print("Todos os números são iguais.")
    
print("-="*30)
print(f"O maior número digitado foi {max(n1, n2, n3)}")
print(f"O menor número digitado foi {min(n1, n2, n3)}")