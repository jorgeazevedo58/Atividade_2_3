'''3 - Crie um programa que leia um arquivo informado pelo usuário, percorrendo cada linha do arquivo e a exibindo na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.'''

import os

def listar_e_ler_arquivo():
    # 1. Listar arquivos .txt no diretório atual
    arquivos = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if not arquivos:
        print("Aviso: Nenhum arquivo .txt encontrado nesta pasta.")
    else:
        print("Arquivos de texto encontrados:")
        for i, arquivo in enumerate(arquivos, 1):
            print(f"{i} - {arquivo}")
    
    # 2. Solicitar o nome ao usuário
    nome_arquivo = input("\nDigite o nome do arquivo que deseja abrir (ou o caminho completo): ")

    # 3. Tentativa de leitura
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"\n--- Exibindo: {nome_arquivo} ---")
            for linha in arquivo:
                print(linha.strip())
                
    except FileNotFoundError:
        print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    listar_e_ler_arquivo()
