from functools import reduce
# Reduce(reduzir)-> acumula e reduz uma lista em um único valor
# não vem dentro do builtins

lista_numeros = [2, 10, 10]
# acumula = 0
# for item in lista_numeros:
#     acumula += item
# print(acumula)

# funcao = lambda acumulador, item: acumulador * item
# resultado = reduce(funcao, lista_numeros, 1)
# print(resultado)

lista = [
    {'produto':'Fone de Ouvido', 'preco' : 500},
    {'produto':'Controle Xbox', 'preco' : 400},
    {'produto':'Celular', 'preco' : 800},
]
funcao = lambda acumulador, produto: acumulador + produto['preco']
resultado = reduce(funcao, lista, 0)
print(resultado)
