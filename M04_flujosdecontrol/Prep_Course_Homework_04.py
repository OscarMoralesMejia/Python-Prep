#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
a=7
if a<0:
    print(f"El número {a} es menor a cero")
else:
    print(f"El número {a} es mayor a cero")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
x=7
y=3.5
tipo_x=type(x)
tipo_y=type(y)
if tipo_x==tipo_y:
    print(f"las variables {x} y {y} son iguales")
else:
    print(f"Las variables {x} y {y} son diferentes")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1,21):
    div=i%2
    if div==0:
        print(f"El número {i} es par")
    else:
        print(f"El número {i} es impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0,6):
    potencia=i**3
    print(f"el número {i} elevado a la tercera potencia es= {potencia}")




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
x=3
for i in range(x):
    print(f"ciclo numero:{i}")




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
numero=5
f=1
if(type(numero)==int):
    if numero>0:
        while numero>0:
            f=numero*f
            numero-=1
        print(f)
    else:
        print("El número proporcionado no es mayor a cero")
else:
    print(f"{numero} no es de tipo entero")




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
x=3
while x>0:
    print(f"ciclo {x} del while ")
    for i in range(2):
        print(f"\tciclo {i} del for")
    x-=1
     




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

for i in range(3):
    x=2
    print(f"\tciclo {i} del for")
    while x>0:
        print(f"ciclo {x} del while")
        x-=1
    





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
limite=30
numero=2
c_primo=0

for j in range(limite+1):
    for i in range(1,numero):
        div=numero%i
        if(div==0):
            c_primo+=1
    if c_primo==1:
        print(f"El número {numero} es primo")
    numero+=1
    c_primo=0
    
 




# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
limite=30
numero=2
c_primo=0

for j in range(limite+1):
    for i in range(1,numero):
        div=numero%i
        if(div==0):
            c_primo+=1
        if c_primo>2:
            break
    if c_primo==1:
        print(f"El número {numero} es primo")
    numero+=1
    c_primo=0




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
#En el número de veces 



# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
min=99
max=300
while min<max:
    min+=1
    div=min%12
    if(div!=0):
        continue
    else:
        print(f"El número {min} es divisible por 12")
        




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
contador=int(input("introduce un número inicial para saber si es número primo"))

limite=30
#contador=1
c_primo=0
while contador<limite:
    for i in range(2,limite+1):
        if contador!=0:
            div=contador%i
            if(div==0):
                c_primo+=1
                break
                #respuesta=input("Deseas continuar(si/no)")
    if c_primo==1 :
        respuesta=input("Deseas conyinuar (si/no)")
        if respuesta=="si":
            print(f"numero primo:{contador}") 
            contador+=1
            c_primo=0
        else: 
            contador+=1
            break



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
min=100
max=300
while min<max:
    div=min%3 
    multiplo=min%6
    if div==0 and multiplo==0:
        print(f"El primer numero divisible por 3 y por 6 es: {min}")
        break
    else:
        min+=1
        continue


