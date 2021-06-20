"""
funções
"""

# totalNotas = 5 + 7 + 5
# media = totalNotas / 3
# print(f'A média da Ana é {media}')


# def calcular_media(nota1, nota2, nota3):
#     totalnotas = nota1 + nota2 + nota3
#     media = totalnotas / 3
#     return media
#     # print(f'A média de {nome_aluno} é {media}')
#
#
# # calcular media do joãozinho
# retorno = calcular_media(8,9,7,)
# print(f'A media de joãozinho é {retorno}')
# # calcular a média da Aninha
# retorno = calcular_media(6,9,9,)
# print(f'A media de Aninha é {retorno}')

alunos = [
    {'nome': 'Jamilton', 'notas': [8, 9, 10]},
    {'nome': 'Ana', 'notas': [7, 10, 10]},
    {'nome': 'João', 'notas': [9, 7, 6]},
]


def calcular_media(notas):
    totalnotas = 0
    for nota in notas:
        totalnotas += nota
    medianota = totalnotas / len(notas)
    return medianota


for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    media = calcular_media(notas)
    print(f'A média de {nome} é {media}')
