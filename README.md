# BDD_ProyectoInventarioMongo
Carlos Collado Calvo DAM01 a Fecha de 24/05/2024

Microproyecto para BDD de una base de datos de una aplicación de gestión de inventario para un taller de reparación de electrodomésticos Se adjuntan tal y como se demanda en la descripción de "Aules" el pdf del trabajo y el archivo js descargables para su lectura y eventual ejecución.

Se recuerda a los posibles usuarios que cualquier problema derivado del uso irresponsable de la información en el documento o a la hora de ejecutar el archivo sql se hace bajo la propia responsabilidad del usuario final y, bajo ningún concepto del creador de los mismos.

Carlos Collado Calvo DAM01 a Fecha de 13/06/2024
=====================================================================
	     GUÍA DE INSTALACIÓN DEL PROGRAMA HIMBENTARIO
=====================================================================

Bienvenido a la Guía de Instalación del programa de gestión de inventario 
de piezas *HIMBENTARIO* (TM)

Asegúrese de leer detenidamente la guía antes de continuar con la instalación.

1.Éste programa sólo ha sido desarrollado para su funcionamiento en entornos 
Linux y con las dependencias que a continuación se detallan:

	1)Docker
	2)MongoDB
	3)Python3
	4)pymongo tkinter
	5)python3-tk
	6)python3-pymongo

2.INSTALACIÓN. Siga PASO A PASO las siguientes puntos para instalar el programa
evitando posibles problemas NOTA: Hasta que no termine cada proceso, no empiece el siguiente
	1) En la terminal de Linux, introducimos los siguientes comandos:
		(1)$ sudo apt-get remove containerd containerd.io
		(2)$ sudo apt-get update
		(3)$ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
		(4)$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
		(5)$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
		(6)$ sudo apt-get update
		(7)$ sudo apt-get install docker-ce docker-ce-cli containerd.io
		(8)$ sudo docker --version
		(9)$ sudo docker run -d -p 27017:27017 --name mongodb mongo
		(10)$ sudo apt-get install python3 python3-pip
		(11)$ pip3 install pymongo tkinter
		(12)$ sudo apt-get install python3-tk
		(13)$ sudo apt-get install python3-pymongo
		(14)$ sudo docker ps
Si en el paso (14)  vemos algo parecido a...

CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                           NAMES
7fe5efde99f5   mongo     "docker-entrypoint.s…"   13 minutes ago   Up 13 minutes   0.0.0.0:27017->27017/tcp, :::27017->27017/tcp   mongodb

...significa que todo marcha bien!

Una vez nos descarguemos himbentario.py de éste mismo repositorio podremos ejecutralo con 
	$ python3 himbentario.py
y podremos empezar a trabajar con él programa

NdA: Actualmente el proyecto se encuentra en su versión 0.1, una alpha en toda regla
altamente inestable y sin pulir. Disculpen las molestias
