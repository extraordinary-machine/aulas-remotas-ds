# funcao_calculadora.py

def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        return numero1 / numero2

# Exemplo
print(calculadora(10, 5, '+'))