'''3 - Crie um programa que sirva para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Cálculo do valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com o usuário: Pede os valores necessários e mostra o resultado formatado.'''

# Programa para calcular o preço final de um produto com desconto

# d - Interação com o usuário: pedir os valores
preco = float(input("Digite o preço do produto: R$ "))
desconto_percentual = float(input("Digite o percentual de desconto (%): "))

# a - Cálculo do desconto
valor_desconto = preco * (desconto_percentual / 100)

# b - Preço final
preco_final = preco - valor_desconto

# c - Formatação: arredondar para 2 casas decimais
preco_final_formatado = round(preco_final, 2)

# Mostrar o resultado
print(f"O valor do desconto foi de R$ {valor_desconto:.2f}")
print(f"O preço final do produto após o desconto é R$ {preco_final_formatado:.2f}")
