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

ping()
