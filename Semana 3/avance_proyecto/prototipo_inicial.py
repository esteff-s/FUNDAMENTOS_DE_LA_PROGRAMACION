
# Inventario de productos para la Papeleria Drupis 

# Contraseña Final :)
Contraseña_Correcta = "1234"

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


# Menu principal

opcion = ""

while opcion != "4":

    print("\n================================")
    print("       PAPELERIA DRUPIS")
    print("      Consulta de inventario")
    print("================================")
    print("1. Ver inventario")
    print("2. Buscar un producto")
    print("3. Calcular costo de productos")
    print("4. Salir")

    opcion = input("Selecciona una opcion: ")

    # OPCION 1: Mostrar inventario 
    if opcion == "1":
        print("\nINVENTARIO DE DRUPIS")
        print("------------------------------")
        print(producto1, "- $", precio1, "- Existencias:", existencia1)
        print(producto2, "- $", precio2, "- Existencias:", existencia2)
        print(producto3, "- $", precio3, "- Existencias:", existencia3)
        print(producto4, "- $", precio4, "- Existencias:", existencia4)
        print(producto5, "- $", precio5, "- Existencias:", existencia5)
        print(producto6, "- $", precio6, "- Existencias:", existencia6)
        print(producto7, "- $", precio7, "- Existencias:", existencia7)
        print(producto8, "- $", precio8, "- Existencias:", existencia8)
        print(producto9, "- $", precio9, "- Existencias:", existencia9)
        print(producto10, "- $", precio10, "- Existencias:", existencia10)
        print(producto11, "- $", precio11, "- Existencias:", existencia11)
        print(producto12, "- $", precio12, "- Existencias:", existencia12)
        print(producto13, "- $", precio13, "- Existencias:", existencia13)
        print(producto14, "- $", precio14, "- Existencias:", existencia14)
        print(producto15, "- $", precio15, "- Existencias:", existencia15)

    # OPCION 2: Buscar un producto
    elif opcion == "2":
        print("\nBUSCAR PRODUCTO")
        print("------------------------------")
        print("1. Libreta cuadro grande")
        print("2. Libreta cuadro chico")        
        print("3. Libreta rayas")
        print("4. Borrador blanco")
        print("5. Sacapuntas")
        print("6. Regla")
        print("7. Pegamento en barra")
        print("8. Tijeras escolares")
        print("9. Paquete de hojas blancas")
        print("10. Pluma negra")
        print("11. Pluma azul")
        print("12. Pluma roja")
        print("13. Marcador negro (Sharpie)")
        print("14. Cartulina")
        print("15. Hojas de foami")



        numero = int(input("Escribe el numero del producto (1 al 15): "))

        if numero == 1:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto1}")
            print("Precio: $", precio1)
            print("Existencias:", existencia1)
            print("================================")

        elif numero == 2:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto2}")
            print("Precio: $", precio2)
            print("Existencias:", existencia2)
            print("================================")

        elif numero == 3:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto3}")
            print("Precio: $", precio3)
            print("Existencias:", existencia3)
            print("================================")

        elif numero == 4:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto4}")
            print("Precio: $", precio4)
            print("Existencias:", existencia4)
            print("================================")

        elif numero == 5:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto5}")
            print("Precio: $", precio5)
            print("Existencias:", existencia5)
            print("================================")

        elif numero == 6:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto6}")
            print("Precio: $", precio6)
            print("Existencias:", existencia6)
            print("================================")

        elif numero == 7:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto7}")
            print("Precio: $", precio7)
            print("Existencias:", existencia7)
            print("================================")

        elif numero == 8:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto8}")
            print("Precio: $", precio8)
            print("Existencias:", existencia8)
            print("================================")

        elif numero == 9:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto9}")
            print("Precio: $", precio9)
            print("Existencias:", existencia9)
            print("================================")

        elif numero == 10:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto10}")
            print("Precio: $", precio10)
            print("Existencias:", existencia10)
            print("================================")

        elif numero == 11:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto11}")
            print("Precio: $", precio11)
            print("Existencias:", existencia11)
            print("================================")

        elif numero == 12:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto12}")
            print("Precio: $", precio12)
            print("Existencias:", existencia12)
            print("================================")

        elif numero == 13:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto13}")
            print("Precio: $", precio13)
            print("Existencias:", existencia13)
            print("================================")

        elif numero == 14:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto14}")
            print("Precio: $", precio14)
            print("Existencias:", existencia14)
            print("================================")

        elif numero == 15:
            print("\n================================")
            print("           PRODUCTO")
            print(f"{producto15}")
            print("Precio: $", precio15)
            print("Existencias:", existencia15)
            print("================================")

        else:
            print("Numero de producto no valido")

    # OPCION 3: Calcular el costo del producto
    elif opcion == "3":

        print("\nCALCULAR COSTO")
        print("------------------------------")
        print("1. Libreta cuadro grande")
        print("2. Libreta cuadro chico")        
        print("3. Libreta rayas")
        print("4. Borrador blanco")
        print("5. Sacapuntas")
        print("6. Regla")
        print("7. Pegamento en barra")
        print("8. Tijeras escolares")
        print("9. Paquete de hojas blancas")
        print("10. Pluma negra")
        print("11. Pluma azul")
        print("12. Pluma roja")
        print("13. Marcador negro (Sharpie)")
        print("14. Cartulina")
        print("15. Hojas de foami")
        numero = int(input("Numero del producto (1 al 15): "))
        cantidad = int(input("Cantidad que solicita el cliente: "))

        if numero == 1:
            print("\n================================")         
            print("           PRODUCTO")
            precio = precio1
            existencia = existencia1
            print("================================")

        elif numero == 2:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio2
            existencia = existencia2
            print("================================")

        elif numero == 3:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio3
            existencia = existencia3
            print("================================")

        elif numero == 4:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio4
            existencia = existencia4
            print("================================")

        elif numero == 5:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio5
            existencia = existencia5
            print("================================")

        elif numero == 6:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio6
            existencia = existencia6
            print("================================")

        elif numero == 7:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio7
            existencia = existencia7
            print("================================")

        elif numero == 8:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio8
            existencia = existencia8
            print("================================")

        elif numero == 9:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio9
            existencia = existencia9
            print("================================")

        elif numero == 10:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio10
            existencia = existencia10
            print("================================")

        elif numero == 11:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio11
            existencia = existencia11
            print("================================")

        elif numero == 12:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio12
            existencia = existencia12
            print("================================")

        elif numero == 13:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio13
            existencia = existencia13
            print("================================")

        elif numero == 14:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio14
            existencia = existencia14
            print("================================")

        elif numero == 15:
            print("\n================================")
            print("           PRODUCTO")
            precio = precio15
            existencia = existencia15
            print("================================")

        else:
            precio = -1
            existencia = 0

        if precio == -1:
            print("Numero de producto no valido")

        elif cantidad <= 0:
            print("La cantidad debe ser mayor que cero")

        elif cantidad > existencia:
            print("No hay suficientes productos disponibles")

        else:
            total = precio * cantidad
            print("Costo total: $", round(total, 2))

    # OPCION 4: Salir del programa
    elif opcion == "4":


        for intento in range (1, 4):
            contraseña = input("Ingresa la contraseña: ")

            if contraseña == Contraseña_Correcta:
                print("Gracias por utilizar el sistema de Papeleria Drupis")
                exit()

            else:
                print("contraseña incorrecta")
                print(f"Intento {intento} de 3")

# Propuesta inicial: Que al poner la contraseña correcta se registren los datos del programa en un archivo .txt (Proximamente...)
#Si no se pone correctamente la contraseña que no se guarde nada y se cierre el programa automaticamente

                

    # Opcion no valida 
    else:
        print("Opcion no valida") 
