print('TUPLAS')
print('Una tupla es una colección de objetos ordenados que encierra sus elementos con paréntesis () \n'
      'y los separa con comas. Las tuplas son muy similares a las listas, y pueden almacenar objetos \n'
      'de tipo distinto como enteros y strings entre otros\n')

print('tomado de:\n https://www.programaenpython.com/fundamentos/tuplas-en-python/#:~:text=Una%20tupla%20es%20una%20colecci%C3%B3n%20de%20objetos%20ordenados,que%20las%20listas%20presentan%20la%20propiedad%20de%20inmutabilidad.')

#Tuplas y operaciones (añadir, listar, remover, actualizar y buscar) con tuplas
print('\n* Añadir un elemento a una tupla \n')
def add_elemento(meses, mes_nuevo):
    return meses + (mes_nuevo,)

meses = ('enero', 'marzo', 'abril', 'mayo')
nuevos_meses = add_elemento(meses, 'junio')
print('meses iniciales:', meses)
print('agregar nuevo mes:', nuevos_meses)

print('\n* Listar elementos de una tupla \n')

def listar_elementos(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ('Karol', 'Edwin','Sebastian' , 'Lorena')
listar_elementos(nombres)

print('\n* Remover elementos de una tupla \n')
def remover_elemento(temperaturas, quitar_temperatura):
    return tuple(e for e in temperaturas if e != quitar_temperatura)

temperaturas = ('11°', '20°', '23°', '35°', '32°', '20°')
quitar_temperatura = '20°'
nuevas_temperaturas = remover_elemento(temperaturas, quitar_temperatura)
print('temperaturas iniciales ', temperaturas)
print('temperaturas finales ', nuevas_temperaturas)


print('\n* actualizar elementos de una tupla \n')


def actualizar_elemento(planetas, pla_original, pla_nuevo):
    return tuple(pla_nuevo if e == pla_original else e for e in planetas)

planetas = ('Mercurio', 'Venus', 'Tierra', 'Marte')

pla_original = 'Tierra'
pla_nuevo = 'planeta Tierra'
planetas_actualizados = actualizar_elemento(planetas, pla_original, pla_nuevo)

print('planetas originales ', planetas)
print('planetas actualizados', planetas_actualizados)


print('\n* buscar elementos de una tupla \n')

def buscar_elemento(autos, buscar_auto):
    for i, e in enumerate(autos):
        if e == buscar_auto:
            return i
    return False

marcas_deportivos = ('Ferrari', 'Lamborghini', 'Porsche', 'McLaren', 'Aston Martin')

buscar_marca = 'Porsche'
resultado = buscar_elemento(marcas_deportivos, buscar_marca)

print('marca a buscar', buscar_marca)
print('marcas ',marcas_deportivos )

if resultado != False:
    print(f"Marca encontrada {marcas_deportivos[resultado]}")
else:
    print("Marca no encontrada")
