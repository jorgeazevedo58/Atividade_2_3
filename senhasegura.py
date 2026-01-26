'''1 - Crie um programa que  gere senhas solicitadas com letras, números e símbolos  e que o usuário também escolha o tamanho da senha para criar senhas seguras automaticamente.'''

import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres possíveis: letras maiúsculas, minúsculas, dígitos e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha escolhendo aleatoriamente 'tamanho' caracteres
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal
print("=== Gerador de Senhas Seguras ===")
tamanho = int(input("Digite o tamanho da senha desejada: "))

senha = gerar_senha(tamanho)
print(f"Sua senha gerada é: {senha}")
