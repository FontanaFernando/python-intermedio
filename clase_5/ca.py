from cb import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = 0.001

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(
                f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}. Saldo: {self.obtener_saldo()}"
            )
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self, monto):
        if monto > 0 and monto <= self.obtener_saldo():
            self._saldo -= monto
            print(
                f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}. Saldo actual: {self.obtener_saldo()}"
            )
        elif monto <= 0:
            print("El monto a extraer debe ser mayor a 0")
        else:
            print("No posee saldo suficiente para esta operación")

    def calcular_interes(self, dias=1):
        # Intereses = Saldo * Tasa * Días / 365
        intereses_ganados = self._saldo * self._tasa_interes * dias / 365
        self._saldo += intereses_ganados
        print(
            f"Se han generado y aplicado {round(intereses_ganados, 2)} de interés. Saldo actualizado: {round(self.obtener_saldo(), 2)}"
        )
        return intereses_ganados
