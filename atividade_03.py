#entrar com os dados dos alunos
# Lista para armazenar os dados dos estudantes
estudantes = []

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Coletar dados dos estudantes
for i in range(5):
    nome = input(f"Digite o nome do estudante {i+1}: ")
    notas = []
    for j in range(3):  # Supondo que cada estudante tenha 3 notas
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    media = calcular_media(notas)
    status = "Aprovado" if media >7 else "Reprovado"
    estudantes.append({'nome': nome, 'media': media, 'status': status})

# Exibir os resultados
for estudante in estudantes:
    print(f"Estudante: {estudante['nome']}, Média: {estudante['media']:.2f}, Status: {estudante['status']}")








