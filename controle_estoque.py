# ================================================
# Controle de Estoque
# Autor: Filipe Martins
# Gerencia estoque de produtos de uma loja
# ================================================

# Dados do estoque
estoque = [
    {"produto": "Teclado",  "preco": 150.0, "quantidade": 5},
    {"produto": "Mouse",    "preco": 80.0,  "quantidade": 12},
    {"produto": "Monitor",  "preco": 900.0, "quantidade": 2},
    {"produto": "Headset",  "preco": 200.0, "quantidade": 0},
    {"produto": "Webcam",   "preco": 350.0, "quantidade": 3},
]

# Produtos disponíveis em estoque
print("--- Produtos disponíveis ---")
for produto in estoque:
    if produto["quantidade"] > 0:
        print(f'{produto["produto"]}: {produto["quantidade"]} Unidades')

# Produtos acima de R$200
print("--- Produtos acima de R$200 ---")
mais_duzentos = [produto["produto"] for produto in estoque if produto["preco"] >= 200.0]
print(mais_duzentos)


def valor_total(estoque):
    """Calcula e imprime o valor total de cada produto no estoque."""
    for produto in estoque:
        nome = produto["produto"]
        total = produto["preco"] * produto["quantidade"]
        print(f"{nome}: R${total:.2f}")


# Valor total por produto

print("--- Valor total por produto ---")
valor_total(estoque)
