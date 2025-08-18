print("-="*30)

desafio = float(input("Qual é a velocidade do carro? "))

if desafio > 80:
    multa = (desafio - 80) *7
    print(f"Você foi multado em R${multa:.2f} por excesso de velocidade.")
else:
    print("Você está dentro do limite de velocidade. Continue dirigindo com segurança!")
print("-="*30)