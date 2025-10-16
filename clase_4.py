class Coche:
    def __init__(self, marca, modelo, color="Crema"):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"El coche {self.marca} {self.modelo} esta encendido.")

    def apagar(self):
        self.encendido = False
        print(f"El coche {self.marca} {self.modelo} esta apagado.")


coche1 = Coche("Renault", 12, "Rojo")
coche2 = Coche("Chevrolet", "Corsa", "Negro")
coche3 = Coche("Fiat", "Regatta")

"""
print(coche1.color)
print(coche2.color)
print(coche3.color)


print(coche1.encendido)
print(coche2.encendido)
coche1.encender()
print(coche1.encendido)
print(coche2.encendido)
coche1.apagar()
print(coche1.encendido)
"""

coche1.encendido = True
print(coche1.encendido)
