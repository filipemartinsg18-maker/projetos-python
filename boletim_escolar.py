# ================================================
# Sistema de Boletim Escolar
# Autor: Filipe Martins
# Processa notas de alunos e gera relatório
# ================================================

# Dados da turma
nomes = ['Ana Silva', 'Filipe Martins', 'Pedro Rosa', 'Diego Lopes']
notas = [
    [8.0, 7.5, 9.0],
    [5.5, 7.9, 8.0],
    [6.0, 3.3, 2.9],
    [7.6, 4.5, 6.8],
]


def calcular_media(notas):
    #Calcula a média e retorna a classificação do aluno.
    media = sum(notas) / len(notas)

    if media >= 7:
        classificacao = "Aprovado"
    elif media >= 5:
        classificacao = "Recuperação"
    else:
        classificacao = "Reprovado"

    return media, classificacao


def gerar_relatorio(nomes, notas):
    #Gera o relatório completo da turma.
    for nome, nota in zip(nomes, notas):
        media, classificacao = calcular_media(nota)
        print(f"Aluno: {nome} | Média: {media:.2f} | {classificacao}")


# Gera o relatório
gerar_relatorio(nomes, notas)
