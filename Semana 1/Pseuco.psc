Algoritmo calculadora_tiempo
	nombre <- ''
	redes <- 0
	mensajeria <- 0
	streaming <- 0
	libros <- 0
	videos <- 0
	spotify <- 0
	tiempo_total <- 0
	porcentaje <- 0
	Escribir '¿Cuál es tu nombre?'
	Leer nombre
	Escribir 'Ingresa las horas dedicadas en redes sociales:'
	Leer redes
	Escribir 'Ingresa las horas de el uso en aplicaciones de mensajeria:'
	Leer mensajeria
	Escribir 'Ingresa las horas de el uso en streaming: '
	Leer streaming
	Escribir 'Ingresa las horas de el uso en libros: '
	Leer libros
	Escribir 'Ingresa las horas de el uso en videos: '
	Leer videos
	Escribir 'Ingresa las horas de el uso en spotify: '
	Leer spotify
	tiempo_total <- redes + mensajeria + streaming + libros + videos + spotify
	porcentaje <- (tiempo_total / 24) * 100
	Escribir ('-----RESUMEN DE TU RUTINA DIGITAL-----')
	Escribir 'Usuario: ', nombre
	Escribir 'Tiempo total en pantalla: ', tiempo_total,' horas'
	Escribir 'Porcentaje de tu día: ', porcentaje, '%'
FinAlgoritmo
