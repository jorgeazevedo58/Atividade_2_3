'''- Crie um programa que consulte informações de uma API, retorne logradouro, bairro, cidade e estado do CEP digitalizado, caso o CEP não exista ou haja erro na requisição, mostre uma mensagem de falha.'''

'''import http.client
import json

def consultar_cep(cep):
    # 1. Conecta ao servidor ViaCEP
    conn = http.client.HTTPSConnection("viacep.com.br")
    
    # 2. Faz a requisição GET
    conn.request("GET", f"/ws/{cep}/json/")
    
    # 3. Recebe a resposta
    response = conn.getresponse()
    
    if response.status == 200:
        dados = json.loads(response.read().decode())
        
        if "erro" in dados:
            print("❌ CEP não encontrado.")
        else:
            print(f"Logradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"Estado: {dados.get('uf')}")
    else:
        print("❌ Falha na requisição da API.")

# Exemplo
consultar_cep("09260430")'''


import urllib.request
import json

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        with urllib.request.urlopen(url) as response:
            dados = json.loads(response.read().decode())
            
            if "erro" in dados:
                print("❌ CEP não encontrado.")
            else:
                print(f"Logradouro: {dados.get('logradouro')}")
                print(f"Bairro: {dados.get('bairro')}")
                print(f"Cidade: {dados.get('localidade')}")
                print(f"Estado: {dados.get('uf')}")
    except Exception as e:
        print(f"❌ Erro: {e}")

# Exemplo
consultar_cep("01001000")



