print("-=" *30)
import random
print("Um professor quer sortear um dos 4 alunos para ajuda-lo a apagar o quadro, poderia ajuda-lo a sortear?  ")

n1 = input("Digite seu nome: ")
n2 = input("Digite seu nome: ")
n3 = input("Digite seu nome: ")
n4 = input("Digite seu nome: ")

nome = n1,n2,n3,n4

escolha = random.choice(nome)

print(f"O sorteio que o professor fez, sorteou o nome {escolha} ")

print("-=" *30)