numeros = [1, 2, 3, 4, 5, 6]
pares_por_dos = [x * 2 for x in numeros if x % 2 == 0]
print(pares_por_dos)

frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
print(erres)