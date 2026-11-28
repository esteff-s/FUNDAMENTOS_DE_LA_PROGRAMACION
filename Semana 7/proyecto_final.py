# ============================================================
# PAPELERIA DRUPIS - Sistema de inventario con archivos
# Problema que resuelve: la papeleria necesita consultar su
# inventario, clientes, ventas y proveedores, calcular el costo
# de una compra y guardar registros sin perderlos al cerrar.
# Hecho por: (escribe aqui tu nombre y matricula)
# Curso: Fundamentos de programacion - Actividad 7
# ============================================================

import time
import os

# Contraseña Final :)
Contraseña_Correcta = "1234"

# ------------------------------------------------------------
# Inventario de productos para la Papeleria Drupis
# ------------------------------------------------------------

# Producto 1
producto1 = "Libreta cuadro grande"
precio1 = 40.00
existencia1 = 25

# Producto 2
producto2 = "Libreta cuadro chico"
precio2 = 35.00
existencia2 = 25

# Producto 3
producto3 = "Libreta rayas"
precio3 = 30.00
existencia3 = 25

# Producto 4
producto4 = "Borrador blanco"
precio4 = 5.00
existencia4 = 15

# Producto 5
producto5 = "Sacapuntas"
precio5 = 10.00
existencia5 = 20

# Producto 6
producto6 = "Regla"
precio6 = 12.00
existencia6 = 8

# Producto 7
producto7 = "Pegamento en barra"
precio7 = 15.00
existencia7 = 20

# Producto 8
producto8 = "Tijeras escolares"
precio8 = 40.00
existencia8 = 6

# Producto 9
producto9 = "Paquete de hojas blancas"
precio9 = 90.00
existencia9 = 15

# Producto 10
producto10 = "Pluma negra"
precio10 = 10.00
existencia10 = 11

# Producto 11
producto11 = "Pluma azul"
precio11 = 10.00
existencia11 = 11

# Producto 12
producto12 = "Pluma roja"
precio12 = 10.00
existencia12 = 11

# Producto 13
producto13 = "Marcador negro (Sharpie)"
precio13 = 25.00
existencia13 = 10

# Producto 14
producto14 = "Cartulina"
precio14 = 5.00
existencia14 = 10

# Producto 15
producto15 = "Hojas de foami"
precio15 = 8.00
existencia15 = 10

# Cada producto es un diccionario, igual que Jugador
datos_productos = [
    (producto1, precio1, existencia1),
    (producto2, precio2, existencia2),
    (producto3, precio3, existencia3),
    (producto4, precio4, existencia4),
    (producto5, precio5, existencia5),
    (producto6, precio6, existencia6),
    (producto7, precio7, existencia7),
    (producto8, precio8, existencia8),
    (producto9, precio9, existencia9),
    (producto10, precio10, existencia10),
    (producto11, precio11, existencia11),
    (producto12, precio12, existencia12),
    (producto13, precio13, existencia13),
    (producto14, precio14, existencia14),
    (producto15, precio15, existencia15),
]

Productos = []
numero_producto = 1
for nombre_p, costo_p, existencia_p in datos_productos:
    Producto = {
        "Numero": numero_producto,
        "Nombre": nombre_p,
        "Costo": costo_p,
        "Existencia": existencia_p
    }
    Productos.append(Producto)
    numero_producto = numero_producto + 1

# ------------------------------------------------------------
# Menus guardados en matrices (lista de listas)
# ------------------------------------------------------------

menu = [
    ["1", "Ver archivos disponibles"],
    ["2", "Ver contenido de un archivo"],
    ["3", "Crear un archivo nuevo"],
    ["4", "Agregar un registro a un archivo"],
    ["5", "Productos"],
    ["6", "Salir"],
]

menu_productos_opciones = [
    ["1", "Ver lista de productos"],
    ["2", "Consultar un producto"],
    ["3", "Calcular costo de una compra"],
    ["4", "Regresar al menu principal"],
]


# ------------------------------------------------------------
# Pedir nombre
# ------------------------------------------------------------

def pedir_nombre():
    """Pide el nombre del usuario y no deja que quede vacio."""
    nombre = ""
    while nombre == "":
        nombre = input("Ingresa tu nombre o nickname: ").strip()
        if nombre == "":
            print("Tienes que escribir un nombre.")
    return nombre

# ------------------------------------------------------------
# Bienvenida y pantalla de carga 
# ------------------------------------------------------------

def bienvenida(nombre):
    """Muestra un mensaje de bienvenida con el nombre del usuario."""
    mensaje = "Bienvenido(a) " + nombre.title() + " a la Papeleria Drupis"
    print("\n" + "=" * len(mensaje))
    print(mensaje)
    print("=" * len(mensaje))


def pantalla_carga():
    """Muestra una barra de carga que se mueve (dura 4 segundos)."""
    for i in range(1, 21):
        barra = "■■" * i
        porcentaje = i * 5
        print("\rCargando " + barra + " " + str(porcentaje) + "%", end="", flush=True)
        time.sleep(0.15)
    print("\n")

# ------------------------------------------------------------
# Fecha y carga
# ------------------------------------------------------------

def pedir_fecha():
    """Pide la fecha dd/mm/aaaa, la revisa y regresa la tupla Fecha."""
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        texto = input("Fecha de operacion (dd/mm/aaaa): ").strip()
        try:
            partes = texto.split("/")
            if len(partes) != 3:
                print("Fecha mal escrita. Ejemplo: 27/11/2026")
                continue
            dia = int(partes[0])
            mes = int(partes[1])
            anio = int(partes[2])
        except ValueError:
            print("La fecha solo debe llevar numeros. Ejemplo: 27/11/2026")
            continue

        if anio < 2000 or anio > 2100:
            print("El anio no es valido.")
        elif mes < 1 or mes > 12:
            print("El mes debe estar entre 1 y 12.")
        else:
            maximo = dias_por_mes[mes - 1]
            # anio bisiesto: febrero tiene 29 dias
            if mes == 2 and anio % 4 == 0:
                maximo = 29
            if dia < 1 or dia > maximo:
                print("Ese dia no existe en ese mes.")
            else:
                Fecha = dia, mes, anio
                return Fecha


def fecha_a_texto(Fecha):
    """Convierte la tupla Fecha a texto, por ejemplo 27/11/2026."""
    dia, mes, anio = Fecha
    return str(dia) + "/" + str(mes) + "/" + str(anio)

# ------------------------------------------------------------
# Mostrar menu
# ------------------------------------------------------------

def mostrar_menu():
    """Dibuja el menu principal recorriendo la matriz."""
    print("\n================================")
    print("       PAPELERIA DRUPIS")
    print("================================")
    for fila in menu:
        print(fila[0] + ". " + fila[1])

# ------------------------------------------------------------
# Inactividad
# ------------------------------------------------------------

def inactividad():
    """Simula 10 minutos sin usar el programa y pregunta si continua."""
    print("\nNo elegiste ninguna opcion...")
    for minuto in range(1, 11):
        print("Minuto", minuto, "de inactividad")
        time.sleep(0.3)
    respuesta = ""
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Pasaron 10 minutos. Deseas continuar? (si/no): ").strip().lower()
        if respuesta != "si" and respuesta != "no":
            print("Solo responde si o no.")
    print("Respuesta recibida:", respuesta)
    return respuesta


# ------------------------------------------------------------
# Archivos
# ------------------------------------------------------------

def pedir_nombre_archivo():
    """Pide un nombre de archivo, le pone .txt y revisa que sea valido."""
    nombre = input("Nombre del archivo: ").strip()
    if nombre == "":
        return ""
    caracteres_malos = '/\\:*?"<>|'
    for letra in nombre:
        if letra in caracteres_malos:
            return ""
    if not nombre.endswith(".txt"):
        nombre = nombre + ".txt"
    return nombre


def listar_archivos():
    """Muestra los .txt de la carpeta en un diccionario numerado."""
    archivos = {}
    numero = 1
    for nombre in os.listdir("."):
        if nombre.endswith(".txt"):
            archivos[numero] = nombre
            numero = numero + 1
    print("\nARCHIVOS DISPONIBLES")
    print("------------------------------")
    for numero in archivos:
        print(numero, "-", archivos[numero])
    return archivos


def ver_archivo():
    """Deja elegir un archivo y muestra lo que tiene adentro."""
    listar_archivos()
    nombre = pedir_nombre_archivo()
    if nombre == "":
        print("Nombre de archivo no valido.")
        return
    try:
        archivo = open(nombre, "r", encoding="utf-8")
        contenido = archivo.read()
        archivo.close()
        print("\n--- " + nombre + " ---")
        print(contenido)
    except FileNotFoundError:
        print("El archivo " + nombre + " no existe.")
    except PermissionError:
        print("No tienes permiso para abrir ese archivo.")
    except Exception:
        print("Ocurrio un error al leer el archivo.")


def crear_archivo(Fecha):
    """Crea un archivo nuevo y escribe la fecha en la primera linea."""
    nombre = pedir_nombre_archivo()
    if nombre == "":
        print("Nombre de archivo no valido.")
        return
    try:
        # modo "x": si el archivo ya existe da error y no lo borra
        archivo = open(nombre, "x", encoding="utf-8")
        archivo.write("# Archivo creado el " + fecha_a_texto(Fecha) + "\n")
        archivo.close()
        print("Archivo " + nombre + " creado.")
    except FileExistsError:
        print("Ese archivo ya existe, no se borro.")
    except PermissionError:
        print("No tienes permiso para crear archivos aqui.")
    except Exception:
        print("Ocurrio un error al crear el archivo.")


def agregar_registro(Fecha):
    """Agrega una linea al final de un archivo sin borrar lo anterior."""
    listar_archivos()
    nombre = pedir_nombre_archivo()
    if nombre == "":
        print("Nombre de archivo no valido.")
        return
    if not os.path.exists(nombre):
        print("El archivo " + nombre + " no existe.")
        return
    registro = input("Escribe el registro (campos separados con |): ").strip()
    if registro == "":
        print("No escribiste nada, no se agrego el registro.")
        return
    try:
        # modo "a": agrega al final sin borrar
        archivo = open(nombre, "a", encoding="utf-8")
        archivo.write(registro + "|" + fecha_a_texto(Fecha) + "\n")
        archivo.close()
        print("Registro agregado.")
    except PermissionError:
        print("No tienes permiso para escribir en ese archivo.")
    except Exception:
        print("Ocurrio un error al escribir en el archivo.")


# ------------------------------------------------------------
# Productos (submenu dentro del menu principal)
# ------------------------------------------------------------

def mostrar_lista_productos():
    """Imprime todos los productos con numero, nombre y costo."""
    print("\n=============================================")
    print("          LISTA DE PRODUCTOS")
    print("=============================================")
    for Producto in Productos:
        print(str(Producto["Numero"]).rjust(2) + " - " +
              Producto["Nombre"].ljust(28) +
              "$ " + "{:.2f}".format(Producto["Costo"]))


def pedir_numero_producto():
    """Pide un numero de producto y regresa el diccionario, o None si no es valido."""
    try:
        numero = int(input("Numero del producto: "))
    except ValueError:
        print("Debes escribir un numero entero.")
        return None
    for Producto in Productos:
        if Producto["Numero"] == numero:
            return Producto
    print("Numero de producto no valido.")
    return None


def consultar_producto():
    """Muestra los datos de un solo producto."""
    mostrar_lista_productos()
    Producto = pedir_numero_producto()
    if Producto is None:
        return
    print("\n---------------------------------------------")
    print("Numero:     ", Producto["Numero"])
    print("Nombre:     ", Producto["Nombre"])
    print("Costo:      $", "{:.2f}".format(Producto["Costo"]))
    print("Existencia: ", Producto["Existencia"])
    print("---------------------------------------------")


def calcular_costo():
    """Calcula el costo de lo que pide el cliente usando la lista Productos."""
    mostrar_lista_productos()
    Producto = pedir_numero_producto()
    if Producto is None:
        return
    try:
        cantidad = int(input("Cantidad que solicita el cliente: "))
    except ValueError:
        print("Debes escribir un numero entero.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
    elif cantidad > Producto["Existencia"]:
        print("No hay suficientes productos disponibles.")
        print("Existencia actual:", Producto["Existencia"])
    else:
        total = Producto["Costo"] * cantidad
        print("Costo total de", cantidad, Producto["Nombre"], ": $", round(total, 2))


def menu_productos():
    """Submenu de productos. Regresa al menu principal con la opcion 4."""
    while True:
        print("\n================================")
        print("       MENU DE PRODUCTOS")
        print("================================")
        for fila in menu_productos_opciones:
            print(fila[0] + ". " + fila[1])

        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            mostrar_lista_productos()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            calcular_costo()
        elif opcion == "4":
            return
        else:
            print("Opcion no valida.")


# ------------------------------------------------------------
# Contraseña
# ------------------------------------------------------------

def pedir_contrasena():
    """Da 3 intentos para la contraseña. Regresa True si es correcta."""
    for intento in range(1, 4):
        clave = input("Ingresa la contraseña: ")
        if clave == Contraseña_Correcta:
            return True
        print("Contraseña incorrecta. Intento", intento, "de 3")
    return False

# ------------------------------------------------------------
# Menu principal y main
# ------------------------------------------------------------

def menu_principal(nombre, Fecha):
    """Ciclo del menu. Regresa "inicio" o "salir" segun lo que pase."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "":
            respuesta = inactividad()

            if respuesta == "no":
                print("Gracias por usar el sistema de la Papeleria Drupis,", nombre.title())
                return "salir"
        elif opcion == "1":
            listar_archivos()
        elif opcion == "2":
            ver_archivo()
        elif opcion == "3":
            crear_archivo(Fecha)
        elif opcion == "4":
            agregar_registro(Fecha)
        elif opcion == "5":
            menu_productos()
        elif opcion == "6":
            if pedir_contrasena():
                print("Gracias por usar el sistema de la Papeleria Drupis,", nombre.title())
                return "salir"
            print("Demasiados intentos. Regresas al menu.")
        else:
            print("Opcion no valida.")


def main():
    """Pantalla de inicio: pide nombre y fecha, carga y abre el menu."""
    nombre = pedir_nombre()
    bienvenida(nombre)
    Fecha = pedir_fecha()
    pantalla_carga()

    resultado = menu_principal(nombre, Fecha)

    if resultado == "salir":
        print("PROGRAMA FINALIZADO")
        return


main()