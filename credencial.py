def read_Cred():
    objeto = {
        "ALICORP" : {
        "myHostname" : "inteliventas.com",
        "myUsername": "alicorp_strategio",
        "myPassword": "auvrdSZymPqV",
        "columnafecha": "3",
        "ruta": "/home/alicorp_strategio/ALICORP"
      },
        "GASAC":{
        "myHostname" : "inteliventas.com",
        "myUsername": "validata_gasac",
        "myPassword": "Validata2193",
        "columnafecha": "3",
        "ruta": "/home/validata_gasac/GASAC"
        },
        "SOFTYS":{
        "myHostname" : "inteliventas.com",
        "myUsername": "validata4144",
        "myPassword": "foodforthought10",
        "columnafecha": "3",
        "ruta": "/home/validata4144/PROTISA"
        }
    
    }
    return objeto
def getCred(BD):
    objeto  = read_Cred()
    myHostname  = objeto[BD]["myHostname"]
    myUsername  = objeto[BD]["myUsername"]
    myPassword  = objeto[BD]["myPassword"]

    return myHostname,myUsername,myPassword

def getColumn(BD):
    objeto  = read_Cred()
    columnafecha  = objeto[BD]["columnafecha"]

    return columnafecha
def getRuta(BD):
    objeto  = read_Cred()
    ruta  = objeto[BD]["ruta"]

    return ruta

