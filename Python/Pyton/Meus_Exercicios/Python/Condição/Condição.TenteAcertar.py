print("-="*30)
import random 

print("Bem vindo ao jogo de adivinhação!")
numero = random.randint(1, 10)  
tentativas = 0
tentativa = int(input("Digite um número entre 1 e 10: "))
print("Tente adivinhar o número entre 1 e 10.")

if tentativa == numero:
    print("Parabéns! Você acertou!, o número era", numero)
else: 
    print(f"O número era {numero}. Tente novamente!")
print("-="*30)