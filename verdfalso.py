import string

def eh_palindromo(texto):
    # 1. Colocar tudo em minúsculas para não diferenciar maiúsculas/minúsculas
    texto = texto.lower()
    
    # 2. Remover espaços e pontuação
    texto = ''.join(ch for ch in texto if ch not in string.punctuation and ch != ' ')
    
    # 3. Comparar o texto com sua versão invertida
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplos de uso:
print(eh_palindromo("A man a plan a canal Panama"))  # Sim
print(eh_palindromo("Olá mundo"))  # Não
print(eh_palindromo("Socorram-me subi no ônibus em Marrocos"))  # Sim
