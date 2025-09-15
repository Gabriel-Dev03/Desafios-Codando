
def mostrarlinha():
    print('-' *30)

mostrarlinha()
print('Função que calcula a área de um terreno')
mostrarlinha()

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {a:.2F}m²')
    mostrarlinha() 

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)

