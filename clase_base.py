from datetime import datetime
from clase_extra_1 import Paciente


class ServicioMedico:
    def __init__(self,fecha, hora, paciente):
        self._precio_estandar = 30
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente


    @property
    def precio_estandar(self):
        return self._precio_estandar


    # fecha
    @property
    def fecha(self):
        return self.fecha

    @fecha.setter
    def fecha(self, n_fecha):
        n_fecha = str(n_fecha).strip()
        try:
            datetime.strptime(n_fecha, '%d/%m/%Y')

        except ValueError:
            raise ValueError('La fecha debe ser válida y tener el formato DD/MM/AAAA.')

        self._fecha = n_fecha



# Hora
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, n_hora):
        n_hora = str(n_hora).strip()
        try:
            datetime.strptime(n_hora, '%H:%M')

        except ValueError:
            raise ValueError('La hora debe ser válida y tener formato HH:MM (ej. 14:30).')

        self._hora = n_hora


    # paciente
    @property
    def paciente(self):
        return self._paciente


    # Validar la instancia de Paciente
    @paciente.setter
    def paciente(self, n_paciente):

        if not isinstance(n_paciente, Paciente):
            raise TypeError('Error: El valor no es una instancia de la clase Paciente.')

        self._paciente = n_paciente


    # Los dos métodos para el encapsulamiento:
    def precio_del_servicio(self):
        return self.precio_estandar

    def es_urgente(self):
        return False



    def __str__(self):
        return f'Datos del servicio médico del paciente\nFecha: {self.fecha}\nHora: {self.hora}hrs\nPaciente: {self.paciente}'