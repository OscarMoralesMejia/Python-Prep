print("Ejercicio 1")
lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
print("resultado ejercicio 2")
for elemento in lista:
    print(elemento)
print("resultado 3")
cadena = "Henry"
for c in cadena:
    print(c)
print("Ejercicio 4")
cadena = "Henry"
for c in enumerate(cadena):
    print(c)
print("Ejercicio 5")
from collections.abc import Iterable
cadena = "Henry"
numero = 9

print("Ejercicio 6")
mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(i)