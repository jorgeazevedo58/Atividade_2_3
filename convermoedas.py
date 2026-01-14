'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Utilize os seguintes dados:

* Valor em reais: R$ 100,00
* Taxa do dólar: R$ 5,20
* Taxa do euro: R$ 6,15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.'''

# O formato {variavel:.2f} garante que o número apareça com 2 casas decimais.

valor_reais = 100.00
taxa_dolar = 5.20 # taxa de cambio do dolar
taxa_euro = 6.15 # taxa de cambio euro
# Fazendo a conversao
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro
# Exibindo os resultados
print(f"Valor em reais: R$ {valor_reais:.2f}") # mostra o valor original
print(f"Valor em dolares: US$ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}") 
