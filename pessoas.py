'''2 - Crie um programa que cria um arquivo com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salve o arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha.'''


import csv
def criar_csv_pessoas():
    caminho_arquivo = r"C:/Exercicios_7/pessoas/pessoas.csv"
    pessoas =[
        ["nome", "Idade", "Cidade"]
        ["Ricardo", 48, "Assis"]
        ["Ric", 48, "Assis"]
        ["Rica", 48, "Assis"]
        ["Cado", 48, "Assis"]

    ]
    try:
        with open(caminho_arquivo, mode="w, newline=", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(pessoas)
            print(f"Arquivo CSV criado em: {caminho_arquivo}")
        except Exception as erro:
            print("Falha ao salvar csv: {caminho_arquivo}")
        criar_csv_pessoas()
