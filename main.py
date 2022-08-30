# lista de diccionarios
listaOrdenadores = [{'id': 1, 'NombrePc': 'Pc1', 'CPU': 'I3'},
                    {'id': 2, 'NombrePc': 'Pc2', 'CPU': 'I5'},
                    {'id': 3, 'NombrePc': 'Pc3', 'CPU': 'I7'},
                    {'id': 4, 'NombrePc': 'Pc3', 'CPU': 'A4'}
                    ]


# función menú
def menuPrincial():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("=== MENÚ PRINCIPAL===")
            print("1. Listar Ordenadores")
            print("2. Añadir Ordenador")
            print("3. Actualizar Ordenador")
            print("4. Eliminar Ordenador")
            print("5. Salir")
            print("=====================")
            opcion = int(input("Selecciones una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, intente de nuevo")

            elif opcion == 5:
                continuar = False
                print("Gracias por usar el sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


# función ejecutar opción seleccionada
def ejecutarOpcion(opcion):
    if opcion == 1:
        try:
            listarOrdenadores()
        except Exception as E:
            print(E)
    elif opcion == 2:
        try:
            anadirOrdenador()
        except Exception as E:
            print(E)
    elif opcion == 3:
        try:
            actualizarOrdenador()
        except Exception as E:
            print(E)
    elif opcion == 4:
        try:
            eliminarOrdenador()
        except Exception as E:
            print(E)
    else:
        print("Error")


def listarOrdenadores():
    for x in listaOrdenadores:
        print("Id Ordenador: {} - Nombre: {} - CPU: {} ".format(x['id'], x['NombrePc'], x['CPU']))
    print("\n")


def anadirOrdenador():
    id = input("Introduzca el id del ordenador: ")
    nom = input("Introduzca el nombre del PC: ")
    cpu = input("Introduzca el CPU del ordenador: ")
    listaOrdenadores.append({'id': id, 'NombrePc': nom, 'CPU': cpu})
    print("Insertado con éxito")
    print("\n ")

def actualizarOrdenador():
    id = int(input("Introduzca el Id del Ordenador a actualizar"))
    nom = input("Introduzca el nuevo nombre del PC: ")
    cpu = input("Introduzca el nuevo CPU del ordenador: ")
    for x in listaOrdenadores:
        if int(x['id']) == id:
            x['NombrePc'] = nom
            x['CPU'] = cpu
    print("\n")
    listarOrdenadores()


def eliminarOrdenador():
    id = int(input("Introduzca el Id del ordenador a eliminar: "))
    contador = 0
    for x in listaOrdenadores:

        if (x['id']) == id:
            del listaOrdenadores[contador]
            print("eliminado")
            contador + 1
    print("\n")
    listarOrdenadores()


###MAIN###
menuPrincial()
