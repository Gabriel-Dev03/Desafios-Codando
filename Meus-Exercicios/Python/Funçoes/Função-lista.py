import random
from time import sleep


def titulo(msg):
    print('-' *(len(msg) + 2))
    print(f'  {msg}')
    print('-' *(len(msg) + 2))

def mostrarLinha():
    print('-' * 30)

# Programa Principal

titulo(' Função Lista ')

numeros = list()
for cont in range(0, 5):
    numeros.append(random.randint(1, 5))

    

def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        print(f'{random.choice(numeros)} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')

def somarPar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


sorteia(numeros)
mostrarLinha()
somarPar(numeros)
mostrarLinha()