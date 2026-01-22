Crie uma função que calcula a gorjeta a ser deixada em um restaurante, com base no valor total da conta e na porcentagem de
gorjeta desejada. Cálculo do valor da gorjeta com base no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retornos: float: O valor da gorjeta calculada'''

Crie uma função que calcula a gorjeta a ser deixada em um restaurante, com base no valor total da conta e na porcentagem de
gorjeta desejada. Cálculo do valor da gorjeta com base no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retornos: float: O valor da gorjeta calculada'''

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta a ser deixada em um restaurante.

    Parâmetros:
    valor_conta (float): O valor total da conta.
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%).

    Retorno:
    float: O valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta