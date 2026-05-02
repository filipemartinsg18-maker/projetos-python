# ================================================
# Agenda de Contatos
# Autor: Filipe Martins
# Gerencia contatos por status e cidade
# ================================================

# Dados dos contatos
contatos = [
    {"nome": "Lucas",   "telefone": "99999-1111", "cidade": "Serra",      "ativo": True},
    {"nome": "Mariana", "telefone": "99999-2222", "cidade": "Vitória",    "ativo": False},
    {"nome": "Rafael",  "telefone": "99999-3333", "cidade": "Serra",      "ativo": True},
    {"nome": "Juliana", "telefone": "99999-4444", "cidade": "Vila Velha", "ativo": True},
    {"nome": "Pedro",   "telefone": "99999-5555", "cidade": "Vitória",    "ativo": False},
]

# Verificar quais contatos estão ativos
print("--- Contatos ativos ---")
for contato in contatos:
    if contato["ativo"]:
        print(f'{contato["nome"]} - {contato["telefone"]}')

# Quais contatos são da Serra
print("--- Contatos de Serra ---")
contatos_serra = [contato["nome"] for contato in contatos if contato["cidade"] == "Serra"]
print(contatos_serra)


def buscar_cidade(contatos, cidade):
    #Busca contatos por cidade e retorna lista de nomes
  
    cidades_especificas = []
    try:
        for contato in contatos:
            if contato["cidade"] == cidade:
                cidades_especificas.append(contato["nome"])
        return cidades_especificas

    except KeyError:
        return "Erro: chave inválida no dicionario."


# Teste de busca por cidade
print("--- Busca por cidade ---")
print(buscar_cidade(contatos, "Vila Velha"))
print(buscar_cidade(contatos, "Vitória"))
