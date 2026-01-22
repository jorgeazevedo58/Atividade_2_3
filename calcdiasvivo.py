'''4 - Crie um programa que calcule a quantos dias um indivíduo está vivo de acordo com os dados do dia.'''

from datetime import datetime

# 1. Solicitar a data de nascimento do usuário
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# 2. Converter a string digitada para um objeto datetime
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

# 3. Obter a data atual
data_atual = datetime.today()

# 4. Calcular a diferença entre as datas
diferenca = data_atual - data_nascimento

# 5. Mostrar o resultado em dias
print(f"Você está vivo há {diferenca.days} dias.")
