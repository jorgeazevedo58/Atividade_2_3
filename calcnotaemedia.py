'''2 - Crie um código para registrar as notas de alunos e calcular a média da turma.'''

# Passo 1: Criar uma lista para armazenar as notas
notas = []

# Passo 2: Definir quantos alunos terão suas notas registradas
quantidade_alunos = int(input("Digite o número de alunos: "))

# Passo 3: Usar um loop para registrar as notas de cada aluno
for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)  # adiciona a nota na lista

# Passo 4: Calcular a média da turma
media = sum(notas) / quantidade_alunos

# Passo 5: Mostrar os resultados
print("\nNotas registradas:", notas)
print(f"Média da turma: {media:.2f}")

