"""
while(condição):
    executa enquanto a condição é verdadeira
"""
# contador = 1
# while contador <= 4:
#     print(f'executou {contador}')
#     contador += 1

postagens = [
    "Hoje passeando pela avenida paulista",
    "Fazendo trilha na pedra do Gavião",
    "hoje fiz um  curso de criação de sistemas",
    "Na casa da mãe, almoçando todos juntos"
]

contador = 0
while contador <=len(postagens) - 1:
    print(f'{contador + 1} - {postagens[contador]}')
    contador += 1
    if contador != len(postagens):
        print("+++++++++++++++++")

