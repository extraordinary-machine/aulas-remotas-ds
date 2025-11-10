# Atividade 1 - Verificador de Maioridade

# 1. Pergunta o nome do usuário
nome = input("Qual é o seu nome? ")

# 2. Pergunta a idade do usuário
idade_texto = input("Qual é a sua idade? ")

# 3. Converte o texto para número inteiro
idade_numero = int(idade_texto)

# 4. Verifica se é maior ou menor de idade
if idade_numero >= 18:
    print(f"Olá, {nome}, você é maior de idade.")
else:
    print(f"Olá, {nome}, você é menor de idade.")
