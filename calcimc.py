'''2- Calculadora de IMC

Desenvolva um programa que calcula o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão do IMC.

< 18.5: classificação = "Abaixo do peso"
< 25: classificação = "Peso normal"
< 30: classificação = "Sobrepeso"
Para os demais cenários: classificação = "Obeso"'''

# Solicita ao usuario o peso em quilogramas
peso = float(input("Digite seu peso em Kg:"))
# Solicita a altura em metros
altura float(input("Digite sua altura em metros:")) # (float) converte esse valor para numero decimal (o resultado pode ter casas decimais).
# Calcula o IMC a formula: peso / altura ao quadrado
imc =peso / (altura ** 2) #Mesmo principio (float pode ter casas decimais)  (**) significa elevado ao quadrado.
# Exibe o valor do IMC calculado
print(f"Seu IMC é: {imc:.2f}")
# Montando extrutura condicional
if imc < 18.5:
    classificalcao = "Abaixo de peso"
elif imc < 25:
    classificalcao = "Peso normal"
elif imc < 30:
    classificalcao = "Sobrepeso"
else:
    classificalcao = "Obeso"

# Exibe a classificação final
print(f"Classificação: {classificalcao}")

