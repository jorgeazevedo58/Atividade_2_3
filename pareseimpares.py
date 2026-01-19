'''4 - Criar um código que sirva para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.'''

# Programa para analisar números digitados pelo usuário
# Classificar como pares ou ímpares e contabilizar cada tipo

# Inicializando os contadores
pares = 0
impares = 0

while True:
    # Solicita um número ao usuário
    numero = int(input("Digite um número (ou -1 para encerrar): "))

    # Condição de parada
    if numero == -1:
        break

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"{numero} é PAR")
        pares += 1
    else:
        print(f"{numero} é ÍMPAR")
        impares += 1

# Exibe o resultado final
print("\nResumo da análise:")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
