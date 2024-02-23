import os


montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

archivo=open('clase09_ej3.csv','w')

lista_llaves=list(montañas.keys())
#archivo.write(str(montañas.keys))
head=''
for item in lista_llaves:
    print(item)
    head+=item+','
head=head[:-1]
archivo.write(head)
archivo.write('\n')

valores=list(montañas.values())

nombres=valores[0]
orden=valores[1]
cordilleras=valores[2]
paises=valores[3]
alturas=valores[4]

for i in range(len(nombres)):
    linea= nombres[i]+','+str(orden[i])+','+cordilleras[i]+','+paises[i]+','+str(alturas[i])
    archivo.write(linea+'\n')
#for item in nombres:
#    print(item)

#    if type(elemento==list):
#        for col in elemento:
#           archivo.write(str(col)+',\n')
archivo.close

