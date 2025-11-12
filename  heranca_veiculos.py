# heranca_veiculos.py

# Classe Pai
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Classe Filha
class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)  # herda os atributos da classe pai
        self.numero_portas = numero_portas

# Exemplo de uso
carro1 = Carro("Toyota", "Corolla", 4)
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Número de portas: {carro1.numero_portas}")