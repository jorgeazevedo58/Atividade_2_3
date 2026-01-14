'''4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não sejam divisíveis por 400.'''

# Programa para verificar se um ano é bissexto

# Solicita ao usuário que insira um ano
ano = int(input("Digite um ano: ")) # (int) converte esse valor para numero inteiro
# (input) pede ao usuario para digitar um numero.

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): # (%) operador de modulo, retorna o resto da divisão.
# (ano % 4 == 0) verifica se o ano e divisivel por 4.
# (ano % 100 != 0) garante que nao seja um ano centenario(como 1900, 2100).
# (ano % 400 == 0) exceção anos centenarios divisiveis por 400 sao bissextos(como 2000, 2400).
    print(f"{ano} é um ano bissexto.") # O (f) é uma f-string,quepermite inserir variaveis diretamente dentro da string.
else:
    print(f"{ano} não é um ano bissexto.")
