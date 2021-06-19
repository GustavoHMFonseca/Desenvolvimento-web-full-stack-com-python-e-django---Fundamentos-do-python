"""
estruturas condicionais
if(se)
else(se não)
"""
idade = 80
condicao = idade >= 18
# criança, adolescente, adulto e idoso
if idade < 13:
    print("criança")
elif idade <= 18:
    print("adolescente")
elif idade <= 65:
    print("adulto")
else:
    print("idoso")

"""
Operadores ternário
"""

idade = 50
# resultado = ('Menor idade', 'Maior idade') [idade >= 18]
resultado = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(resultado)
