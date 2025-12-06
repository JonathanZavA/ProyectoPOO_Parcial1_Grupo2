class Paciente:
    def __init__(self,nombre,apellido,edad,genero,correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.correo = correo

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, n_nombre):
        n_nombre = ' '.join(str(n_nombre).split())
        if not n_nombre:
            raise ValueError('El apellido no puede estar vacío')
        if not n_nombre.replace(' ','').isalpha():
            raise ValueError('El parámetro no ´puede contener numeros ni carácteres especiales.')
        self._nombre = n_nombre 

    # Apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, n_apellido):
        n_apellido = ' '.join(str(n_apellido).split())

        if not n_apellido:
            raise ValueError('El apellido no puede estar vacío.')

        if not n_apellido.replace(' ','').isalpha():
            raise ValueError('El parámetro no puede contener numeros ni carácteres especiales.')

        self._apellido = n_apellido


    # Edad
    @property
    def edad(self):
        return self._edad


    @edad.setter
    def edad(self, n_edad):
        str_edad = str(n_edad).replace(' ','')

        if str_edad.isdigit():
            n_edad = int(str_edad)

            if 0 <= n_edad <= 123:
                self._edad = n_edad
            else:
                raise ValueError('La edad no está dentro del rango permitido.')
        else:
            raise ValueError('Error: El numero tiene que ser positivo y unicamente entero, enténtelo de nuevo.')



    #Genero
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, n_genero):
        n_genero = str(n_genero).lower().strip()
        if n_genero not in ('m', 'f'):
            raise ValueError('No está dentro de los valores permitidos (m,f)')

        self._genero = n_genero


    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, n_correo):
        n_correo = str(n_correo).strip()

        if not n_correo or ' ' in n_correo:
            raise ValueError('El correo no puede estar vacío ni contener espacios.')

        dividido = n_correo.split('@')

        if len(dividido) != 2 or '.' not in dividido[1] or not dividido[0] or not dividido[1]:
            raise ValueError('Formato de correo inválido.')

        self._correo = n_correo




    def __str__(self):
        # Devuelve los datos en una sola línea limpia
        return f"Datos del paciente\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}\nGénero: {self._genero}\nCorreo: {self._correo}"


paciente1 = Paciente('nombre','apellido',9,'m','jonmat@gmail.com')
print(paciente1.nombre)