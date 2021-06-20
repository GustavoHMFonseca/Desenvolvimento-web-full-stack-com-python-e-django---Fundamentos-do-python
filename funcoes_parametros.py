# múltiplos parâmetros (packing)

def somar(*numeros):
    print(type(numeros))
    total = 0
    for numero in numeros:
        total += numero
    print(f'total: {total}')


# somar(1, 10, 9)

# múltiplos parâmetros(unpacking)

# def calcular_media(nota1, nota2):
#     media = (nota1 + nota2)/2
#     print(f'Média: {media}')


# notas = [10,8]
# notas = (10,8)
# notas = {10,8}
# calcular_media(*notas)

# parâmetro opcionais e nomeados

def calcular_media2(nota1,nota2, ponto_extra=0, nota_extra =0):# valor opcional
    media = (nota1 + nota2)/2 + ponto_extra
    print(f'Média: {media} extra: {nota_extra}')


calcular_media2(10,10, nota_extra = 5)# parâmetro nomeado

