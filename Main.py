class Evento:
    def __init__(self, nombre, fecha, duracion, num_participantes, num_jueces):
        self.nombre = nombre
        self.fecha = fecha
        self.duracion = duracion
        self.num_participantes = num_participantes
        self.num_jueces = num_jueces

class SedeOlimpica:
    def __init__(self, nombre, presupuesto_aproximado):
        self.nombre = nombre
        self.presupuesto_aproximado = presupuesto_aproximado
        self.complejos = []

    def agregarComplejo(self, complejo):
        self.complejos.append(complejo)
        
class ComplejoDeportivo:
    def __init__(self, nombre, tipo, localizacion, jefe_organizacion, area_total):
        self.nombre = nombre
        self.tipo = tipo
        self.localizacion = localizacion
        self.jefe_organizacion = jefe_organizacion
        self.area_total = area_total
        self.eventos = []

    def agregarEvento(self, evento):
        self.eventos.append(evento)

#----- SEDE COMPLETA 1----------
evento1 = Evento("Carrera de 100m", "2024-08-01", "00:10:00", 8, 3)
evento2 = Evento("Salto de longitud", "2024-08-02", "00:30:00", 12, 5)

complejo1 = ComplejoDeportivo("Estadio Olímpico", "Polideportivo", "Centro", "Juan Perez", 10000)
complejo1.agregarEvento(evento1)
complejo1.agregarEvento(evento2)

complejo2 = ComplejoDeportivo("Piscina Olímpica", "Deporte único", "EsquinaNE", "Maria Gomez", 5000)
complejo2.agregarEvento(evento2)

sede_olimpica = SedeOlimpica("Tokyo 2024", 1000000)
sede_olimpica.agregarComplejo(complejo1)
sede_olimpica.agregarComplejo(complejo2)
# FIN SEDE 1-----------------

#----- SEDE COMPLETA 2----------
evento3 = Evento("Natación 20 metros", "2024-08-01", "00:10:00", 8, 3)
evento4 = Evento("Futbol", "2024-08-02", "00:60:00", 24, 3)
evento5 = Evento("Tenis", "2024-08-02", "00:20:00", 2, 2)

complejo3 = ComplejoDeportivo("Complejo olimpico de Quito", "Polideportivo", "Sur", "Carlos Orellana", 500000)
complejo3.agregarEvento(evento3)
complejo3.agregarEvento(evento4)
complejo3.agregarEvento(evento5)

sede_olimpica1 = SedeOlimpica("Ecuador 2024", 500000)
sede_olimpica1.agregarComplejo(complejo3)
# FIN SEDE 2-----------------

#----- SEDE COMPLETA 3----------
evento6 = Evento("Nado de 100m", "2024-10-30", "00:20:00", 6, 5)
evento7 = Evento("Garrocha", "2024-11-12", "00:30:00", 10, 5)

complejo4 = ComplejoDeportivo("Piscina Olímpica", "Deporte único", "Norte", "Cristina Reinoso", 50000)
complejo4.agregarEvento(evento6)

complejo5 = ComplejoDeportivo("Pista de Atletismo", "Polideportivo", "Centro", "Franciso Mosquera", 8000)
complejo5.agregarEvento(evento7)

sede_olimpica2 = SedeOlimpica("Colombia 2024", 58000)
sede_olimpica2.agregarComplejo(complejo4)
sede_olimpica2.agregarComplejo(complejo5)
# FIN SEDE 3-----------------


#ARRAY DE SEDES
arraySedes = [sede_olimpica, sede_olimpica1, sede_olimpica2]

#ARRAY DE COMPLEJOS
arrayComplejos = [complejo1, complejo2, complejo3, complejo4, complejo5]

#ARRAY DE EVENTOS
arrayEventos = [evento1, evento2, evento3, evento4, evento5, evento6, evento7]

def listarSedes():
   for i, sede in enumerate(arraySedes):
      print(f"{i+1}. {sede.nombre}")

def listarComplejos():
   for i, complejo in enumerate(arrayComplejos):
      print(f"{i+1}. {complejo.nombre}")

def listarEventos():
   for i, evento in enumerate(arrayEventos):
      print(f"{i+1}. {evento.nombre}")



def listar_all(sede_olimpica):
    print("Información de la Sede Olímpica:", sede_olimpica.nombre)
    print("Presupuesto aproximado:", sede_olimpica.presupuesto_aproximado)
    print("Número de complejos:", len(sede_olimpica.complejos))
    print("")
    for complejo in sede_olimpica.complejos:
        print("Nombre del complejo:", complejo.nombre)
        print("Tipo de complejo:", complejo.tipo)
        print("Localización:", complejo.localizacion)
        print("Jefe de organización:", complejo.jefe_organizacion)
        print("Área total ocupada:", complejo.area_total)
        print("Eventos:")
        for evento in complejo.eventos:
            print("  - Nombre:", evento.nombre)
            print("    Fecha:", evento.fecha)
            print("    Duración:", evento.duracion)
            print("    Número de participantes:", evento.num_participantes)
            print("    Número de jueces:", evento.num_jueces)
            print("")
 
def mostrarMenuPrincipal():
    while True:
        print("\033[1m------> PROYECTO FINAL <-------\033[0m")
        print("")
        print("\033[1mPrograma para mostrar información de eventos que se desarrollarán en distintas sedes.\033[0m")
        print("Menu principal:")
        print("1. Listar Sedes")
        print("2. Listar Complejos")
        print("3. Listar Eventos")
        print("4. Listar información detallada de cada sede")
        print("5. Finalizar programa")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("")
            print("")
            print("\033[1mLISTA DE SEDES EXISTENTES:\033[0m")
            listarSedes()
            print("")
            print("")
        elif opcion == '2':
            print("")
            print("")
            print("\033[1mLISTA DE COMPLEJOS EXISTENTES:\033[0m")
            listarComplejos()
            print("")
            print("")
        elif opcion == '3':
            print("")
            print("")
            print("\033[1mLISTA DE EVENTOS EXISTENTES:\033[0m")
            listarEventos()
            print("")
            print("")
        elif opcion == '4':
            print("")
            print("")
            print("\033[1mLISTA DE SEDES EXISTENTES:\033[0m")
            listarSedes()
            print("")
            print("")
            sedeIndex = int(input("Seleccione el número de la sede para obtener información: ")) - 1
            if 0 <= sedeIndex < len(arraySedes):
                print("")
                print("")
                print("\033[1mINFORMACIÓN DETALLADA DE LA SEDE:\033[0m")
                listar_all(arraySedes[sedeIndex])
                print("")
                print("")
            else:
                print("Número de sede no válido.")
            print("")
            print("")
        elif opcion == '5':
            print("Finalizando el Programa.....")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    mostrarMenuPrincipal()
