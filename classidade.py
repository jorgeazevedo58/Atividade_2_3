'''1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).'''


# Solicita a idade do usuario
idade = int(input("Digite sua idade: ")) # input() pede ao usuario que digite algo. 
# int() converte o valor digitado (que vem com texto)para numero inteiro.

# Extrutura condicional para a idade
if idade >= 0 and idade <= 12: # Verifica se a idade esta entre 0 e 12
    print("Voce e uma Criança.")
elif idade >= 13 and idade <= 17: # (elif)significa "senão, se" verifica se a idade esta entre 13 e 17.
    print("Voce e Adolecente.")
elif idade >= 18 and idade <= 59:
    print("Voce e Adulto")
elif idade >= 60:
    print("Voce e um Idoso")
else:
    print("Idade invalida. digite um numero positivo")