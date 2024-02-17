class Funciones:
    def __init__(self,lista_num):
        self.lista=lista_num
        
        
    def __esprimo(self,num):
        i=2
        flag=True
        while i< num:
            if num%i==0:  
                flag=False
                break
            i+=1
        return flag
    
    def detectaprimos(self):
        '''
        Funcion para detectar los números primos
        '''
        for item in self.lista:
            if self.__esprimo(item)==True:
                 print('El elemento', item, 'SI es un numero primo')
            else:
                print('El elemento', item, 'NO es un numero primo')       

    def masrepite(self):
        i=0
        contados=[]
        repeticiones=[]
        marca=0
        ranking={"numero":"","repeticiones":""}
        for elemento in self.lista:
            #while i<len(lista): 
            veces=self.lista.count(elemento)
            #print(lista.count(elemento))
            if veces>1 and contados.count(elemento)==0:
                contados.append(elemento)
                repeticiones.append(veces)
        for i,item in enumerate(repeticiones):
            l=len(repeticiones)
            for e in repeticiones:
                if item >e:
                    marca+=1
                if marca==l-1:
                    valor=e
                    break
        print(valor)
        indice=repeticiones.index(valor)
        numero=contados[indice]
        print(numero)
        rank=[numero,valor]
        return rank#contados,repeticiones
    
    def conversion_grados(self,origen,destino):
        for i in self.lista:
            print(i," grados seran convertidos de: ",origen,"a ",self.__convertidorTemperatura(i,origen,destino),destino)
    def __convertidorTemperatura(self,grados,origen,destino):
        resultado=grados
        if origen.upper()=="CELSIUS" and destino.upper()=="FARENHEIT":
            resultado=32+(grados*(9/5))
        elif origen.upper()=="CELSIUS" and destino.upper()=="KELVIN":
            resultado=273.15+grados
        elif origen.upper()=="FARENHEIT" and destino.upper()=="CELSIUS":
            resultadoc=(grados-32)*(5/9)
        elif origen.upper()=="FARENHEIT" and destino.upper()=="KELVIN":
            resultado=((grados-32)*5/9)+273.15
        elif origen.upper()=="KELVIN" and destino.upper()=="CELSIUS":
            resultado=grados-273.15
        elif origen.upper()=="KELVIN" and destino.upper()=="FARENHEIT":
            resultado=((grados-273.15)*(9/5))+32
        elif origen.upper()==destino.upper():
            resultado=grados
        else:
            print("opción no reconocida")
        return resultado
    def factorial(self):
        for i in self.lista:
            print("El factorial de ",i,"es",self.__factorial(i))
    def __factorial(self,numero):
        if numero>0 and type(numero)==int:
            if numero<=1:
                return 1
            numero=numero*self.__factorial(numero-1)
        else:
            print("Solo se aceptan números enteros positivos")
            return
        return numero