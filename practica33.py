class Activo:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

class Pasivo:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

class Persona:
    TIPO_IDENTIFICACION_CEDULA = "C"
    TIPO_IDENTIFICACION_RUC = "R"

    def __init__(self, identificacion, tipo_identificacion):
        self.identificacion = identificacion
        self.tipo_identificacion = tipo_identificacion

    def __str__(self):
        return "%s" % self.identificacion

    def imprimir_informacion(self):
        print("%s" % self.tipo_identificacion)
        print("%s" % self.identificacion)

class PersonaNatural(Persona):
    def __init__(self, cedula,nombres, apellidos, edad):
        Persona.__init__(self, cedula, Persona.TIPO_IDENTIFICACION_CEDULA)
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)

    def imprimir_informacion(self):
        Persona.imprimir_informacion(self)
        print("%s" % self.nombres)
        print("%s" % self.apellidos)
        print("%d" % self.edad)

class PersonaJuridica(Persona):
    def __init__(self, ruc ,razon_social):
        Persona.__init__(self, ruc, Persona.TIPO_IDENTIFICACION_RUC)
        self.razon_social = razon_social

    def __str__(self):
        return "%s" % (self.razon_social)

    def imprimir_informacion(self):
        Persona.imprimir_informacion(self)
        print("%s" % self.razon_social)


# pn1 = PersonaNatural("0543150", "Frank", "Malo", 30)
# pn2 = PersonaNatural("099999", "Juan", "Peralta", 50)
# pn3 = PersonaNatural("088888", "Pepe", "Sanchez", 70)
# pn1.imprimir_informacion()

class Cliente(PersonaNatural, PersonaJuridica):
    TIPO_PERSONA_NATURAL = 1
    TIPO_PERSONA_JURIDICA = 2

    def __init__(self, tipo_persona, activos, pasivos, **args):
        self.tipo_persona = tipo_persona
        self.activos = activos
        self.pasivos = pasivos

        if tipo_persona == self.TIPO_PERSONA_NATURAL:
            PersonaNatural.__init__(self, args["cedula"], args['nombres'], args['apellidos'], args["edad"] )
        else:
            PersonaJuridica.__init__(self, args["ruc"], args['razon_social'])

    def imprimir_informacion(self):
        if self.tipo_persona == self.TIPO_PERSONA_NATURAL:
            PersonaNatural.imprimir_informacion(self)
        else:
            PersonaJuridica.imprimir_informacion(self)

    def obtenerPatrimonio(self):
        patrimonio = 0
        for activo in self.activos:
            patrimonio += activo.valor

        for pasivo in self.pasivos:
            patrimonio -= pasivo.valor

        return patrimonio


# cl1 = Cliente(Cliente.TIPO_PERSONA_JURIDICA, ruc="0963135435", razon_social="ESPOL")
# cl1.imprimir_informacion()
print("#################################3")

activos = []
pasivos = []

activos.append(Activo("casa", 80000))
activos.append(Activo("auto", 25000))

pasivos.append(Pasivo("prestamo h", 50000))
pasivos.append(Pasivo("tarjeta", 3000))

cl2 = Cliente(Cliente.TIPO_PERSONA_NATURAL, activos, pasivos ,cedula="1351351",nombres="Freank", apellidos="Malo", edad=30)
cl2.imprimir_informacion()
print(cl2.obtenerPatrimonio())