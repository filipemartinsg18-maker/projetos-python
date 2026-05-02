# ================================================
# Catálogo de Filmes
# Autor: Filipe Galter
# Buscar filmes por gênero usando dicionários
# ================================================

# Filmes e seus dados
filmes = [
    {"titulo": "Interestelar", "nota": 9.2, "genero": "Ficção científica"},
    {"titulo": "Parasita",     "nota": 8.5, "genero": "Drama"},
    {"titulo": "John Wick",    "nota": 7.1, "genero": "Ação"},
    {"titulo": "Midsommar",    "nota": 6.8, "genero": "Terror"},
    {"titulo": "Soul",         "nota": 8.9, "genero": "Animação"},
]


def buscar(filmes, genero):
    #Busca filmes por gênero e retorna lista de títulos.
    genero_lista = []
    try:
        for filme in filmes:
            if filme["genero"] == genero:
                genero_lista.append(filme["titulo"])
        return genero_lista

    except KeyError:
        return "Erro: chave inválida no dicionário."


# Teste do código
print(buscar(filmes, "Drama"))
print(buscar(filmes, "Animação"))
print(buscar(filmes, "Ação"))
