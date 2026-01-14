'''3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

def converter_temperatura(valor, origem, destino):# (def) é uma função
    # Normaliza para minúsculas
    origem = origem.lower() # Converte tudo para minuscula para evitar problema com maiusculas/minisculas
    destino = destino.lower()

    # Primeiro converte para Celsius
    if origem == "celsius": #(==) significa comparação de igualdade
        celsius = valor
    elif origem == "fahrenheit":
        celsius = (valor - 32) * 5/9
    elif origem == "kelvin":
        celsius = valor - 273.15
    else:
        return "Unidade de origem inválida!"

    # Agora converte de Celsius para a unidade desejada
    if destino == "celsius":
        return celsius
    elif destino == "fahrenheit":
        return (celsius * 9/5) + 32
    elif destino == "kelvin":
        return celsius + 273.15
    else:
        return "Unidade de destino inválida!"


# Programa principal
valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (Celsius, Fahrenheit, Kelvin): ")
destino = input("Digite a unidade de destino (Celsius, Fahrenheit, Kelvin): ")

resultado = converter_temperatura(valor, origem, destino)
print(f"{valor} {origem} = {resultado:.2f} {destino}")