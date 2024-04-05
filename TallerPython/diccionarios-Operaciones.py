# Creamos un diccionario
diccionario = {'nombre': 'Diego', 'edad': 24, 'ciudad': 'Popayan'}

# Añadimos un elemento al diccionario
diccionario['pais'] = 'Colombia'
print(diccionario)  # {'nombre': 'Diego', 'edad': 24, 'ciudad': 'Popayan', 'pais': 'Colombia'}

# Listamos los elementos
for key, value in diccionario.items():
    print(key, value)

# Removemos o eliminamos el elemento pais
del diccionario['pais']
print(diccionario)  # {'nombre': 'Diego', 'edad': 24, 'ciudad': 'Popayan'}

# Actualizamos el elemento ciudad
diccionario['ciudad'] = 'Medellín'
print(diccionario)  # {'nombre': 'Diego', 'edad': 24, 'ciudad': 'Medellín'}

# Buscamos el elemento Diego
print(diccionario.get('nombre'))  # 'Diego'