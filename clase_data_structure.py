# Algoritmo que pregunta 10 frutas o verduras y las almacena
# en lo que es nuestra canasta de mandado
# Se pueden repetir
# Ejemp: Manzana, Uvas...

MAX_GROS = 10
groceries = []

for count in range(MAX_GROS):
	item = input(f'Objeto {count + 1} de la lista: ')
	# Metodos de manejo de strings (Estudiar)
	item_lower = item.lower()
	groceries.append(item_lower)
	# groceries.append(input(f'Objeto {count + 1}' de la lista: ).lower()) - Otra forma de hacer la linea 12 mas avanzadamente

print('\nTu mandado quedo: ')
print(groceries)

for grocery in groceries:
	print(grocery)

print('Leo estuvo aquí')


