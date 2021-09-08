import pysftp 
import os 
import datetime
from credencial import getCred

def getRutasSftp(Corporativo,ruta) :
    data = []
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys= None
    myHostname,myUsername,myPassword = getCred(Corporativo)

    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword,cnopts=cnopts) as sftp:
        print ("Obteniendo Lista de DISTRIBUIDORAS ")

        # Cambiar a directorio remoto
        sftp.cwd(ruta)

        # Obtener estructura del directorio '/var/www/vhosts'
        directory_structure = sftp.listdir_attr()

        # Imprimir información
        for attr in directory_structure:
            # print (attr.filename)
            data.append(attr.filename)
    return data


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

    
        