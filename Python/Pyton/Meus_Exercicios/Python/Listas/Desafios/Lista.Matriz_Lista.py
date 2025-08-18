matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    soma_linha = sum(matriz[i])
    soma_coluna = sum(matriz[j][i] for j in range(3))
    print(f"Linha {i+1} soma: {soma_linha}, Coluna {i+1} soma: {soma_coluna}")
