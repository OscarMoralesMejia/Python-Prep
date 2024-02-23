import sys as s
import os 
from datetime import datetime, date, time, timezone

if len(s.argv)==4:
    temperatura=s.argv[1]
    humedad=s.argv[2]
    lluvia=s.argv[3]
    #print(str(datetime.now(timezone.utc)))
    marca_de_tiempo=datetime.now(timezone.utc)
    #print(type(marca_de_tiempo))
    marca_de_tiempo=datetime.timestamp(marca_de_tiempo)
    #print(type(marca_de_tiempo))
    #print(type(temperatura))
    #print(type(humedad))
    #print(type(lluvia))
    linea_texto=str(marca_de_tiempo)+','+temperatura+','+humedad+','+lluvia
    
    archivo=open('clase09_ej2.csv','a')
    archivo.write(linea_texto+"\n")
    archivo.close()
    
else:
    print("Debe introducir los parametros en el siguiente orden:temperatura(grados centigrados),humedad(texto),lluvia(boolean)")
