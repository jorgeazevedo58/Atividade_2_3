'''2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Utilize as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50,00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.'''

'''nome_produto = "Camiseta" # Nome do produto
preco_original = 50.00  # Preço original em reais
porcentagem_desconto = 20  # Porcentagem de desconto (%)

# Calculo do desconto

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibindo Resultados

print(f"produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Percentual de desconto: {porcentagem_desconto}%")
print(f"Valor de desconto: R$" {valor_desconto:.2f}")
print(f"Preço final : R$ {preco_final:.2f}")'''


# Calculadora de Desconto
# Este programa calcula o valor do desconto aplicado em um produto
# e mostra o preço final após o desconto.

# -----------------------------
# 1. Definição dos dados iniciais
# -----------------------------
nome_produto = "Camiseta"   # nome do produto
preco_original = 50.00      # preço original em reais
percentual_desconto = 20    # porcentagem de desconto (%)

# -----------------------------
# 2. Cálculo do desconto
# -----------------------------
# O desconto é calculado multiplicando o preço pelo percentual/100.
valor_desconto = preco_original * (percentual_desconto / 100)

# O preço final é o preço original menos o valor do desconto.
preco_final = preco_original - valor_desconto

# -----------------------------
# 3. Exibição dos resultados
# -----------------------------
# O print mostra todos os detalhes formatados com 2 casas decimais.
print(f"Produto: {nome_produto}")  
print(f"Preço original: R$ {preco_original:.2f}")  
print(f"Percentual de desconto: {percentual_desconto}%")  
print(f"Valor do desconto: R$ {valor_desconto:.2f}")  
print(f"Preço final com desconto: R$ {preco_final:.2f}")  