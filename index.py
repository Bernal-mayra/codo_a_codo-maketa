#TrabajoFinal - Codoacodo - BernalMayra - 2023
import json


def elegir_carrera():   
    carreras = {
        1 : '- Prof. de inicial',
        2 : '- Interprete de LSA',
        3 : '- Prof. de Primaria',
        4 : '- Prof. de Historia',
        5 : '- Prof. de Matematica'}
    for clave, valor in carreras.items():
        print(clave, valor) 
    while True:
        try:
            carrera = int(input('Elija una Carrera'))
            break
        except ValueError:
            print('El valor ingresado no es numerico, vuelva a intentarlo')
    carrera = (carreras[carrera])
    print(carrera)
    return carrera

def materias():
    tiene_materias = input('¿Tiene materias aprobadas? s/n: ')
    if tiene_materias == 's' or tiene_materias =='S':
        materias_aprobadas = {}
        while tiene_materias =='s':
            materia = input('ingrese nombre de la materia: ')
            while True:
                try:
                    nota = int(input('Ingrese la nota final: '))
                    break
                except ValueError:
                    print('El valor ingresado no es numerico, vuelva a intentarlo')
            materias_aprobadas.update({materia : nota})
            print(materias_aprobadas)
            tiene_materias = input('¿Quiere agregar otra materia? s/n: ')
    elif tiene_materias == 'n':
        materias_aprobadas = {'Aun no tiene materias aprobadas': ' '}
    return materias_aprobadas

def alumno_regular():
    while True:
        alumnoregular = input("¿Es alumno regular? s/n: ")
        if alumnoregular == "s":
            alumnoregular = True
            break
        elif alumnoregular == 'n':
            alumnoregular = False
            break
        else:
            print('Elija una opcion valida')
        return alumno_regular

def cargar_base_estudiantes():
    try:
        with open('datos_estudiantes.json','r') as archivo:
            datos_estudiantes = json.load(archivo)
    except FileNotFoundError:
        datos_estudiantes = []
    return datos_estudiantes

def guardar_base_estudiantes(datos_estudiantes):
    with open('datos_estudiantes.json', 'w') as archivo:
        json.dump(datos_estudiantes, archivo, indent=4)

def carga_estudiante():  
    print("Carga DE datos de un estudiantes: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fdn = input('Fecha de nacimiento (dd-mm-aaaa):')
    print("Fecha de Nacimiento: ",fdn)

    while True:
        try:
            dni = int(input("Ingrese el numero de Dni: "))
            edad = int(input("Su edad: "))
            break
        except ValueError:
            print('No ingresaste un valor valido, vuelve a intentarlo: ')

    direccion = input("Introduce la direccion: ")
    email = input("Correo electronico: ")
            
    carrera = elegir_carrera() #ELECCION DE LA CARRERA
    
    alumnoregular = alumno_regular() #Eleccion True o false

    #INGRESO de MATERIAS APROBADAS
    materias_aprobadas = materias()

    #diccionario con los datos del estudiante nuevo
    dato_estudiante = {'id' : dni,
                        'nombre' : nombre,
                        'apellido' : apellido, 
                        'dni' : dni,
                        'edad' : edad,
                        'fdn' : fdn,
                        'direccion' : direccion,
                        'email' : email, 
                        'carrera' : carrera, 
                        'alumnoregular' : alumnoregular,
                        'materias_aprobadas' : materias_aprobadas}
    
    #carga los datos del estudiante 
    datos_estudiantes = cargar_base_estudiantes ()
    datos_estudiantes.append(dato_estudiante)
    guardar_base_estudiantes (datos_estudiantes)
    print('Estudiante guardado en la base de datos.')
    
    seguir_carga = input("Agregar otro/a estudiante s/n: ")
    while True:
        if seguir_carga == 's':
            carga_estudiante()
        elif seguir_carga == 'n':
            menu_muestra()
            break
    return datos_estudiantes

def ver_Lista_est():
    datos_estudiantes = cargar_base_estudiantes()
    if datos_estudiantes:
        for id in datos_estudiantes:
            print(id)
        #busca
    else:
        print("No hay datos de estudiantes almacenados.")
    menu_muestra()
    return
    
def buscar_est(dni, datos_estudiantes): # PARA MODIFICAR O ELIMINAR
    '''busca el dicccionario con datos (dni == id) del estudiante //
    PARA MODIFICAR O ELIMINAR'''
    indice = None
    for i, dato_estudiante in enumerate(datos_estudiantes):
        if dato_estudiante['id'] == dni:
            indice = i
            break
    return indice

def eliminar_estudiantes():
    dni = int(input("Ingrese el nro. de DNI (sin puntos) del estudiante que desea eliminar: "))
    datos_estudiantes = cargar_base_estudiantes()
    indice = buscar_est(dni, datos_estudiantes)

    if indice is not None:
        print(datos_estudiantes[indice])
        confirmar = input('Esta segurx de eliminar a este estudiante s/n: ')
        while confirmar == 's':
            del datos_estudiantes[indice]
            guardar_base_estudiantes(datos_estudiantes)
            print("estudiante eliminado exitosamente.")
    else:
        print("No se encontró el contacto.")
    seguir_carga = input("Eliminar otro/a estudiante s/n: ")
    while True:
        if seguir_carga == 's':
            eliminar_estudiantes()
        elif seguir_carga == 'n':
            menu_muestra()

def modificar_datos_est():
    seguir = 's'
    while seguir == 's':
        while True: #busca el id = dni
                    try:
                        dni = int(input("Ingrese el nro. de DNI (sin puntos) del estudiante que desea modificar: "))
                        break
                    except ValueError:
                        print('El valor ingresado no es numerico, vuelva a intentarlo')

        datos_estudiantes = cargar_base_estudiantes()
        indice = buscar_est(dni, datos_estudiantes)

        if indice is not None:
            otro = 's'
            while otro == 's':
                print('DATOS DEL ESTUDIANTE: ')
                print(datos_estudiantes[indice])

            #OPCIONES PARA MODIFICAR:
                print('Ingrese lo que desea modificar')
                dato_estudiante = {1 : 'dni',
                                    2 : 'edad',
                                    3 : 'nombre',
                                    4 : 'apellido',
                                    5 : 'fdn',
                                    6 : 'direccion',
                                    7 : 'email',
                                    8 : 'carrera',
                                    9 : 'alumnoregular',
                                    10 : 'materias_aprobadas'}        
            #muetra las opciones: 
                for clave, valor in dato_estudiante.items():
                    print(clave, valor) 

                while True: #var dato
                    try:
                        dato = int(input('Ingrese la opcion que desea modificar: '))
                        break
                    except ValueError:
                        print('El valor ingresado no es correcta, vuelva a intentarlo')

                if dato >= 11: #error al ingresar
                    print('El valor ingresado no es valido, vuelve a intentar')
                
                else: #opciomes para modificar            
                    dato = (dato_estudiante[dato])
                    print(dato)

                #NUMERICAS:
                    #edad
                    if dato == "edad":
                        print('Se modificara la Edad: ')
                        while True:
                            try:
                                dato_mod = int(input('Ingrese el dato: '))
                                break
                            except ValueError:
                                print('El valor ingresado no es numerico, vuelva a intentarlo')
                    #id/dni
                    elif dato == "dni":
                        print('Se modificara el DNI:')

                        while True:
                            try:
                                dato_mod = int(input('Ingrese el nuevo DNI: '))
                                break
                            except ValueError:
                                print('El valor ingresado no es numerico, vuelva a intentarlo')

                        datos_estudiantes[indice]['id'] = dato_mod
                        guardar_base_estudiantes(datos_estudiantes)
                #DATOS PERSONALES cad.
                    elif dato == "nombre":
                        print('Se modificara el/los nombre/s (Colocar el nombre completo)')
                        dato_mod = input('Ingrese el/los nombres: ')
                    elif dato == "apellido":
                        print('Se modificara el/los apellido/s (Colocar el nombre completo)')
                        dato_mod = input('Ingrese el/los apellidos: ')
                    elif dato == "fdn":
                        print('Se modificara la fecha de nacimiento(dd-mm-aaaa)')
                        dato_mod = input('Ingrese la fecha de nacimiento: ')
                    elif dato == "direccion":
                        print('Se modificara la direccion')
                        dato_mod = input('Ingrese la nueva direcccion: ')
                    elif dato == "email":
                        print('Se modificara el correo electronico (ejemplo@extencion.com')
                        dato_mod = input('Ingrese el correo electronico: ')
                #CARRERA
                    elif dato == "carrera":
                        print('Se modificara la carrera')  
                        dato_mod = elegir_carrera()
                #ALUMNO REGULAR
                    elif dato == "alumnoregular":
                        print('Se modificara el dato de su regularidad como alumno')
                        dato_mod = alumno_regular()   
                #MATERIAS
                    elif dato == "materias_aporobadas":                     
                        print(dato_estudiante)
                        dato_mod = materias()
                    datos_estudiantes[indice][dato] = dato_mod
                    guardar_base_estudiantes(datos_estudiantes)
                    print("Contacto actualizado exitosamente.")
                otro = input('Desea modificar algo mas? s/n') #Bandera
            seguir = input('Desea modificar otro estudiante? s/n')
        else:
            print('No se encuentra el estudiante, vuelva a intentar')
    menu_muestra()

def menu_muestra():
    """Las opciones del menu"""
    print('''
    \t :::Menú del sistema de Gestion de Estudiantes:::
    1 - Ver lista de estudiantes
    2 - Agregar nuevos estudiantes
    3 - Modificar datos
    4 - Eliminar estudiantes
    5 - Salir''')
    accion_menu()

def accion_menu():
    """interaccion del usuario con el menu"""
    opcion_menu = 0
    while opcion_menu <= 5:
        while True:
            try:
                opcion_menu = int(input("Ingrese una opción:  "))
                break
            except ValueError:
                print("no valido, intente otra vez")
            
        if opcion_menu == 1:
            ver_Lista_est()
        elif opcion_menu == 2:
            carga_estudiante()
        elif opcion_menu == 3:
            modificar_datos_est()
        elif opcion_menu == 4:
            eliminar_estudiantes()
        elif opcion_menu == 5:
            print('Gracias por usar el sistema de Gestion de Estudiantes')
            break
        else:
            print('Opción no valida, ingrese las opciones disponibles')
            menu_muestra()
    
    return

        

#main
menu_muestra()
