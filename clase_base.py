from datetime import datetime
from clase_extra_1 import Paciente

class ServicioMedico:


    def __init__(self,fecha, hora, paciente):
        """ Constructor de la clase. Inicializa y valida los datos"""
        # Se define el valor del precio estandar.
        self._precio_estandar = 30

        # Asignamos a través de los setters (sin guin bajo) para validar al instanciar
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente

    @property
    def precio_estandar(self):
        return self._precio_estandar


    @property
    def fecha(self):
        """Getter para obtener la fecha."""
        return self.fecha


    @fecha.setter
    def fecha(self, n_fecha):
        """Setter para validar el formato de fecha (DD/MM/AAAA)."""
        n_fecha = str(n_fecha).strip()
        try:
            datetime.strptime(n_fecha, '%d/%m/%Y')
        except ValueError:
            raise ValueError('La fecha debe ser válida y tener el formato DD/MM/AAAA.')
        self._fecha = n_fecha


    @property
    def hora(self):
        """Getter para obtener la hora."""
        return self._hora


    @hora.setter
    def hora(self, n_hora):
        """Setter para validar el formato de hora (HH:MM)."""
        n_hora = str(n_hora).strip()
        try:
            datetime.strptime(n_hora, '%H:%M')
        except ValueError:
            raise ValueError('La hora debe ser válida y tener formato HH:MM (ej. 14:30).')
        self._hora = n_hora


    @property
    def paciente(self):
        """Getter para obtener el objeto paciente."""
        return self._paciente


    @paciente.setter
    def paciente(self, n_paciente):
        """Setter para validar que el objeto sea instancia de Paciente."""
        if not isinstance(n_paciente, Paciente):
            raise TypeError('Error: El valor no es una instancia de la clase Paciente.')
        self._paciente = n_paciente


    # Métodos para el encapsulamiento

    def precio_del_servicio(self):
        """Retorna el precio estándar definido en la constante."""
        return self.precio_estandar


    def es_urgente(self):
        """
            Indica si el servicio es urgente.
             Por defecto es False en la clase padre.
        """
        return False


    def __str__(self):
        """Retorna la información del objeto."""
        return f'Datos del servicio médico del paciente\nFecha: {self.fecha}\nHora: {self.hora}hrs\nPaciente: {self.paciente}'



