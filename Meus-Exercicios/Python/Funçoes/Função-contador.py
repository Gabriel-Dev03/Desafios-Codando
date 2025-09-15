from time import sleep

def mostrarLinha():
    print('-' * 30)


def titulo(msg):
    print('-' *(len(msg) + 4))
    print(f'  {msg}')
    print('-' *(len(msg) + 4))

titulo(' Função Contador ')


def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            
            print(f'{cont} ', end='',flush=True)
            sleep(0.3)
            cont += passo
        print('FIM!')
        
    else:
        Cont = inicio
        while Cont >= fim:
            
            print(f'{Cont} ', end='',flush=True)
            sleep(0.3)
            Cont -= passo
        print('FIM!')
          
    
# Programa Principal
contador(1, 10, 1)
mostrarLinha()  
contador(10, 0, 2)
mostrarLinha()
print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))
contador(ini, fim, pas)