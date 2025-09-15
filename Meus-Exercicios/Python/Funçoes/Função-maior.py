from time import sleep


def titulo(msg):
    print('-' *(len(msg) + 2))
    print(f'  {msg}')
    print('-' *(len(msg) + 2))

def fim(msg):
    print('-' *(len(msg) + 2))
    print(f'  {msg}')
    print('-' *(len(msg) + 2))


def mostrarLinha():
    print('-' * 30)

titulo(' Função Maior ')

def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
mostrarLinha()
maior(2, 9, 4, 5, 7, 1)
mostrarLinha()
maior(4, 7, 0)
mostrarLinha()
maior(1, 2)
mostrarLinha()
maior(6, 1, 8, 2, 3, 4, 5)
mostrarLinha()

fim(' Fim do Programa ')
mostrarLinha()