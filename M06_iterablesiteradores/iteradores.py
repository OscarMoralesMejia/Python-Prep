libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))

lista_1 = [1, 2, 3]
lista_2 = ['a', 'b', 'c']
combinacion = zip(lista_1, lista_2)

for item in combinacion:
    print(item)