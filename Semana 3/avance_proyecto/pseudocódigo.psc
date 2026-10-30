Algoritmo PapeleriaDrupis
	
    Definir Contrasena_Correcta, contrasena, opcion Como Caracter
    Definir nombres Como Caracter
    Definir precios, total Como Real
    Definir existencias, numero, cantidad, intento, i Como Entero
    Definir correcta Como Logico
	
    Dimension nombres[15], precios[15], existencias[15]
	
    Contrasena_Correcta <- "1234"
	
	nombres[1] <- "Libreta cuadro grande"
	precios[1] <- 40
	existencias[1] <- 25
	
	nombres[2] <- "Libreta cuadro chico"
	precios[2] <- 35
	existencias[2] <- 25
	
	nombres[3] <- "Libreta rayas"
	precios[3] <- 30
	existencias[3] <- 25
	
	nombres[4] <- "Borrador blanco"
	precios[4] <- 5
	existencias[4] <- 15
	
	nombres[5] <- "Sacapuntas"
	precios[5] <- 10
	existencias[5] <- 20
	
	nombres[6] <- "Regla"
	precios[6] <- 12
	existencias[6] <- 8
	
	nombres[7] <- "Pegamento en barra"
	precios[7] <- 15
	existencias[7] <- 20
	
	nombres[8] <- "Tijeras escolares"
	precios[8] <- 40
	existencias[8] <- 6
	
	nombres[9] <- "Paquete de hojas blancas"
	precios[9] <- 90
	existencias[9] <- 15
	
	nombres[10] <- "Pluma negra"
	precios[10] <- 10
	existencias[10] <- 11
	
	nombres[11] <- "Pluma azul"
	precios[11] <- 10
	existencias[11] <- 11
	
	nombres[12] <- "Pluma roja"
	precios[12] <- 10
	existencias[12] <- 11
	
	nombres[13] <- "Marcador negro (Sharpie)"
	precios[13] <- 25
	existencias[13] <- 10
	
	nombres[14] <- "Cartulina"
	precios[14] <- 5
	existencias[14] <- 10
	
	nombres[15] <- "Hojas de foami"
	precios[15] <- 8
	existencias[15] <- 10
	
	Mientras opcion <> "4" Hacer
		
        Escribir ""
        Escribir "================================"
        Escribir "       PAPELERIA DRUPIS"
        Escribir "      Consulta de inventario"
        Escribir "================================"
        Escribir "1. Ver inventario"
        Escribir "2. Buscar un producto"
        Escribir "3. Calcular costo de productos"
        Escribir "4. Salir"
        Escribir "Selecciona una opcion: "
        Leer opcion
		
        Segun opcion Hacer
			
            Caso "1":
                Escribir "INVENTARIO DE DRUPIS"
                Para i <- 1 Hasta 15 Con Paso 1 Hacer
                    Escribir nombres[i], " - $", precios[i], " - Existencias: ", existencias[i]
                FinPara
				
            Caso "2":
                Escribir "BUSCAR PRODUCTO"
                Para i <- 1 Hasta 15 Con Paso 1 Hacer
                    Escribir i, ". ", nombres[i]
                FinPara
                Escribir "Escribe el numero del producto (1 al 15): "
                Leer numero
                Si numero >= 1 Y numero <= 15 Entonces
                    Escribir "================================"
                    Escribir "           PRODUCTO"
                    Escribir nombres[numero]
                    Escribir "Precio: $", precios[numero]
                    Escribir "Existencias: ", existencias[numero]
                    Escribir "================================"
                Sino
                    Escribir "Numero de producto no valido"
                FinSi
				
            Caso "3":
                Escribir "CALCULAR COSTO"
                Para i <- 1 Hasta 15 Con Paso 1 Hacer
                    Escribir i, ". ", nombres[i]
                FinPara
                Escribir "Numero del producto (1 al 15): "
                Leer numero
                Escribir "Cantidad que solicita el cliente: "
                Leer cantidad
				
                Si numero < 1 O numero > 15 Entonces
                    Escribir "Numero de producto no valido"
                Sino
                    Si cantidad <= 0 Entonces
                        Escribir "La cantidad debe ser mayor que cero"
                    Sino
                        Si cantidad > existencias[numero] Entonces
                            Escribir "No hay suficientes productos disponibles"
                        Sino
                            total <- precios[numero] * cantidad
                            Escribir "Costo total: $", Redon(total * 100) / 100
                        FinSi
                    FinSi
                FinSi
				
            Caso "4":
                intento <- 1
                correcta <- Falso
                Mientras intento <= 3 Y correcta = Falso Hacer
                    Escribir "Ingresa la contrasena: "
                    Leer contrasena
                    Si contrasena = Contrasena_Correcta Entonces
                        Escribir "Gracias por utilizar el sistema de Papeleria Drupis"
                        correcta <- Verdadero
                    Sino
                        Escribir "Contrasena incorrecta"
                        Escribir "Intento ", intento, " de 3"
                        intento <- intento + 1
                    FinSi
                FinMientras
				
            De Otro Modo:
                Escribir "Opcion no valida"
				
        FinSegun
		
    FinMientras
	
FinAlgoritmo