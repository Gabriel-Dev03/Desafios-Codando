print("-=" * 30)
import random
print(" O mesmo professor do Desafio.EscolhaRandom quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.")

n1 = input("Digite seu nome: ")
n2 = input("Digite seu nome: ")
n3 = input("Digite seu nome: ")
n4 = input("Digite seu nome: ")

nomes = n1,n2,n3,n4

ordem = random.sample(nomes, len(nomes))

print(f"O sorteio considerou que a apresentação seria conforme os nomes digitados: {ordem}")