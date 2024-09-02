## Ejercicio 2

Para este ejercicio utilizaré python.

1. Verifique si un conjunto de servidores (dadas sus direcciones ip) están accesibles desde la red local.

Sabemos que para hacer ping a una ip se usa el comando:
    
````shell 
ping -c 1 <ip>
````

Para ello utilizamos la libreria 'os' de python y el comando 'ping' para verificar si un servidor está accesible.

````python
import os

#verificar si un conjunto de servidores estan activos desde red local
def ping():
    #ip de servidores (ejemplo)
    ips = ['172.28.112.1']
    #servidores activos
    activos = []
    #servidores inactivos
    inactivos = []
    #ping a servidores
    for ip in ips:
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            activos.append(ip)
        else:
            inactivos.append(ip)
    print("Servidores activos: ", activos)
````
Para ejecutar la función 'ping' simplemente llamamos a la función.

````python
ping()
`````

Salida:
````shell
Haciendo ping a 172.28.112.1 con 32 bytes de datos:
Respuesta desde 172.28.112.1: bytes=32 tiempo<1m TTL=128
Respuesta desde 172.28.112.1: bytes=32 tiempo<1m TTL=128
Respuesta desde 172.28.112.1: bytes=32 tiempo<1m TTL=128
Respuesta desde 172.28.112.1: bytes=32 tiempo<1m TTL=128

Estadísticas de ping para 172.28.112.1:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 0ms, Máximo = 0ms, Media = 0ms
Servidores activos:  ['172.28.112.1']

Process finished with exit code 0
````
