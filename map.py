# Map -> Mapear os dados, percorrer e alterá-los
lista_numero = [10,20,30]

# nova_lista = map(lambda n: n*2, lista_numero)
# print(type(nova_lista))
# print(list(nova_lista))


lista = [
    {'produto':'Fone de Ouvido', 'preco' : 500},
    {'produto':'Controle Xbox', 'preco' : 400},
    {'produto':'Celular', 'preco' : 800},
]


def calcular_desconto(produto):
    produto['preco'] -= 10
    return produto


nova_lista = map(calcular_desconto, lista)
print(list(nova_lista))
