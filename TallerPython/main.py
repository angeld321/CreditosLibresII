# ---------- Metodos De Cadenas (Strings) ----------

# capitalize(): Convierte el primer carácter en mayúscula
nombre = "firulais"
print(nombre.capitalize())


# casefold(): Convierte la cadena a minúsculas ideal para comparaciones

string = "Firulais Lindo Perrito"
print(string.casefold())


# count(): Cuenta cuántas veces aparece una subcadena

string = "wof wof wau wof wau wau wof"
print(string.count("wof"))


# find(): Encuentra la una primera subcadena dada y devuelve su indice

string = "hola firulais"
print(string.find("firulais"))


# format(): Reemplaza en la cadena campos de sustitución por valores dados

nombreDueño = "Angel"
nombrePerro = "Firulais"

print("{} es dueño de {}".format(nombreDueño, nombrePerro))


# lower(): Convierte toda la cadena a minúsculas

string = "FIRULAIS ROBA PAN"
print(string.lower())


# upper(): Convierte toda la cadena a mayúsculas

string = "firulais hermosooo"
print(string.upper())


# partition(): Divide la cadena en tres partes usando la primera aparición de una subcadena

string = "hola firulais"
print(string.partition(","))


# replace(): Reemplaza todas las apariciones de una subcadena con otra

string = "Firulais perrito lindo"
print(string.replace("lindo", "feo"))

# split(): Divide la cadena en una lista de subcadenas con separador

string = "Firulais hace wof"
print(string.split(" "))
