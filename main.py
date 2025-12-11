#-Integrantes:
#-ZAVALA ALCIVAR JONATHAN ISRAEL
#- REYES OBANDO DANIELA ALEJANDRA
#- PINTADO CORREA SYLVIA ANGELICA
from clase_hija_1 import ConsultaGeneral
from clase_hija_2 import Urgencia
from clase_extra_1 import Paciente
from clase_extra_2 import Gestor
from clase_base import ServicioMedico

def main():
    gestor = Gestor()

    paciente1 = Paciente("Ana", "Lopez", 30, "f", "ana@gmail.com")
    paciente2 = Paciente("Mario", "Perez", 40, "m", "mperez@gmail.com")

    consulta1 = ConsultaGeneral("10/10/2024", "08:00", paciente1, "Cardiología")
    urgencia1 = Urgencia("11/10/2024", "09:30", paciente2, "alta")

    gestor.agregar_servicio(consulta1)
    gestor.agregar_servicio(urgencia1)

    urgentes, no_urgentes = gestor.clasificar_servicios()

    print("=== SERVICIOS URGENTES ===")
    for s in urgentes:
        print(s)
        print()

    print("=== SERVICIOS NO URGENTES ===")
    for s in no_urgentes:
        print(s)
        print()

    total = gestor.calcular_total_gastos()
    print(f"Total acumulado a pagar por todos los servicios: ${total:.2f}")


if __name__ == "__main__":
    main()

