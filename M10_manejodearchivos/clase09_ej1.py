import sys as s

if len(s.argv)==4:
    for e,i in enumerate(s.argv):
        print(f"{i} es el parametro número: {e}")
else:
    print("ERROR: Se deben introducir 3 partametros")
    print("Ejemplo: clase09_ej1.py 2 3 4")