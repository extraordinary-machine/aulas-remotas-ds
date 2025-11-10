# Atividade 2 - A Tabuada

# 1. Pede um número e converte para inteiro
numero_str = input("Digite um número para ver a tabuada: ")
numero = int(numero_str)

print(f"\n--- Tabuada do {numero} ---")

# 2. Usa um loop for de 1 até 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
