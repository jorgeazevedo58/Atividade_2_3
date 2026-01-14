'''4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Gasto combustível: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.'''
distancia_percorrida = 300
combustivel_gasto = 25
consumo_medio = distancia_percorrida / combustivel_gasto
print("Distancia percorrida: ", distancia_percorrida, "km")
print("Combustivel gasto: ", combustivel_gasto, "litros")
print("Consumo medio:", round(consumo_medio, 2), "Km/l")
print(f"Consumo medio: {consumo_medio:.3f}", "km/l")