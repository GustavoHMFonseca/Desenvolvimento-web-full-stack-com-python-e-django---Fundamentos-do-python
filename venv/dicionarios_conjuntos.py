"""
Lista e Tuplas: indexadas
lista = ["joão", "maria"]
lista: 0 -> "joão", 1->"maria"
"""

# dicionario = {
#     'correr': 'Deslocar-se ou mover-se rapidamente',
#     'ligar' : 'Estabelecer uma comunicação',
# }
#
# print(dicionario['correr'])

carro = {
    'modelo': 'Fusca',
    'marca': 'volkswagen',
    'ano': 1970,
    'donos':['marcos','maria']
}

#print(type(carro))
# carro['donos'].append('Pedro')
# print(carro['donos'][0])

# carro['km'] = 8500
# print(carro['km'])

#carro['ano'] = 1980
#carro.update({'ano':1980, 'km': 8500})
#del carro['ano']
# valor = carro.pop('ano')
# print(valor)
# print(carro.keys())
# print(carro.values())
# print(carro.items())
# print(carro.get('km', 'padrao'))
# print(len(carro))
# carro.clear()
# print(carro)

"""
set -> conjunto
"""

# itens = {"Gustavo", "José", "Maria", 4, "Maria"}
# lista = ["Gustavo", "José", "Maria", 4, "Maria"]
#
# #print(type(itens))
# print(lista)

carros = {"fusca", "gol", "fiat 147"}
# carros2 = {"BMW", "fusca", "passat"}
# novo = carros.union(carros2)
# novo = carros.intersection(carros2)
# carros.add('BMW')
carros.remove('fusca')
print(carros)


