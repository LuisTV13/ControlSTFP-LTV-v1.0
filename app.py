import os
import glob
import os,time
from credencial import getRuta
from credencial import getColumn
from sftp  import *
import pysftp 
import pandas as pd
import zipfile
import numpy as np


Corporativo = 'GASAC' 
ruta = str(getRuta(Corporativo))

data = getRutasSftp(Corporativo,ruta)
# print(data)
lend = len(data)
log = ''
cnopts = pysftp.CnOpts()
cnopts.hostkeys= None
myHostname,myUsername,myPassword= getCred(Corporativo)
info = []

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword,cnopts=cnopts) as sftp:
        print ("Connection succesfully stablished ... ")
        # for n in data:
        for i in range(0,lend):
        # Cambiar a directorio remoto
                sftp.cwd(ruta+'/'+data[i]+'/')

                # Obtener estructura del directorio '/var/www/vhosts'
                directory_structure = sftp.listdir_attr()
                remoteFile = ruta+'/'+data[i]+'/output.zip'
                localfile = 'output/output.zip'
                extract ='extrac/'
                password = None
                # Imprimir información
                for attr in directory_structure:
                    if attr.filename == 'output.zip':
                       
                    # print(a)
                       
                        sftp.get(remoteFile,localfile)
                        
                        archivo_zip = zipfile.ZipFile(localfile,"r")
                        try:
                            print(data[i])
                            print(archivo_zip.namelist())
                            archivo_zip.extractall(path=extract,pwd=password)
                        except: 
                            pass
                        archivo_zip.close()
                        
                        #Leemos el Csv de Ventas
                        try:
                            rutadf = 'extrac/Ventas.csv'
                            columnafecha = getColumn(Corporativo)
                            df = pd.read_csv(rutadf , header=None ,sep ='|',dtype=np.object0 )

                            k=max(df[int(columnafecha)])
                        except:
                            k='Sin Venta'
                            print(k)




                        a = Corporativo,data[i],attr.filename,attr.st_size,time.strftime("%d-%m-%Y" ,time.localtime(attr.st_mtime)),time.strftime("%H:%M" ,time.localtime(attr.st_mtime)),k


                        info.append(a)
                        
                        ex = 'extrac/*'
                        files = glob.glob(ex)
                        for f in files:
                            os.remove(f)
                    else:
                        print("======ARCHIVOS APARTE========")
                        print(attr.filename)
                        print("==============================")

columnas =['CORPORATIVO','DISTRIBUIDOR','ARCHIVO','PESOARCHIVO','FECHA','HORA','ULTIMAFECHAVENTA']
df = pd.DataFrame(info ,columns=columnas) 
print(df)
tabla =df.pivot_table(index=['CORPORATIVO','DISTRIBUIDOR','ARCHIVO','FECHA','HORA','ULTIMAFECHAVENTA'])

print(tabla)
tabla.to_excel('excel/Controlenvio_'+Corporativo+'_SFTP'+'.xlsx',sheet_name='data',startrow=1)

