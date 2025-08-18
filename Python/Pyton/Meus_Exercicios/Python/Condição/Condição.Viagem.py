print("-="*30)
preco = 0
distancia = float(input("Qual é a distância da sua viagem em km? "))
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print(f"O preço da sua passagem é R${preco:.2f} para uma viagem de {distancia} km.")
print("-="*30)