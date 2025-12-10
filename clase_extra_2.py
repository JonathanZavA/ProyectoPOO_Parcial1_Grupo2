class Gestor:
    def __init__(self):
        # aquí se guardan TODOS los servicios
        self.servicios = []
        self.urgentes = []
        self.no_urgentes = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def clasificar_servicios(self):

        for servicio in self.servicios:
            if servicio.es_urgente():
                self.urgentes.append(servicio)
            else:
                self.no_urgentes.append(servicio)

        return self.urgentes, self.no_urgentes

    def calcular_total_gastos(self):
        total = 0
        for servicio in self.servicios:
            total += servicio.calcular_gasto()
        return total

    def __str__(self):
        return f'Servicios registrados: {self.servicios}\nUrgentes:{self.urgentes}\nNo urgentes:{self.no_urgentes}'



if __name__ == '__main__':
    gestor = Gestor
    print(gestor)