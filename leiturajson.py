'''- Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não exista ou ocorra erro ao salvar, mostre uma mensagem de falha.'''

import json
import os

def gerenciar_dados():
    arquivo_nome = 'dados_usuario.json'
    
    # 1. Criando o dicionário com as informações
    dados = {
        "nome": "Jorge Silva",
        "idade": 58,
        "cidade": "Santo Andre"
    }

    try:
        # 2. Escrevendo no arquivo JSON
        with open(arquivo_nome, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Arquivo salvo com sucesso!")

        # 3. Lendo o arquivo JSON
        if os.path.exists(arquivo_nome):
            with open(arquivo_nome, 'r', encoding='utf-8') as arquivo:
                dados_lidos = json.load(arquivo)
            
            print("\n--- Dados Recuperados ---")
            print(f"Nome: {dados_lidos['nome']}")
            print(f"Idade: {dados_lidos['idade']}")
            print(f"Cidade: {dados_lidos['cidade']}")
        else:
            print("Erro: O arquivo não foi encontrado para leitura.")

    except (IOError, OSError) as e:
        # 4. Tratamento de falhas
        print(f"Falha na operação: {e}")

if __name__ == "__main__":
    gerenciar_dados()