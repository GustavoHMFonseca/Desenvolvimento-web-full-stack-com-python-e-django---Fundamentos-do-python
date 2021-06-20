"""
Funções como objetos de primeira classe, são funções que se
comportam como qualquer tipo nativo de uma determinada linguagem.
"""

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

# lista = [somar, subtrair]
# for funcao in lista:
#     resultado = funcao(5, 6)
#     print(f'Resultado: {resultado}')

# a = somar
# print(a(1,2))

"""
Funções de ordem superior são funções que recebem funções como
parâmetro(s) e/ou retornam funções como resposta
"""

carrinho_compras = [
    {'produto':'Fone de Ouvido', 'preco' : 500},
    {'produto':'Controle Xbox', 'preco' : 400},
    {'produto':'Celular', 'preco' : 800},
]

print(carrinho_compras)


def calcular_desconto(lista, funcao):
    for produto in lista:
        #print(produto['preco'])
        item_desconto = funcao(produto['preco'], 10)
        print(item_desconto)


calcular_desconto(carrinho_compras,subtrair)
