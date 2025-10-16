from cb import CuentaBancaria


class CuentaCorriente(CuentaBancaria):
    def __init__(
        self,
        nombre_titular,
        dni_titular,
        fecha_nacimiento,
        saldo=0,
        limite_extraccion=500,
    ):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion

    def extraer(self, monto):
        if monto <= 0:
            print("El monto a extraer debe ser mayor a 0")
            return
        if monto > self.obtener_saldo():
            print("Usted no posee saldo suficiente para realizar la operación")
        elif monto > self._limite_extraccion:
            print(
                f"Usted no puede extraer {monto}. Su límite de extracción diario es de {self._limite_extraccion}"
            )
        else:
            self._saldo -= monto
            print(
                f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}. Saldo actual: {self.obtener_saldo()}"
            )

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(
                f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}. Saldo: {self.obtener_saldo()}"
            )
        else:
            print("El monto a depositar debe ser mayor a 0")
