lista = [1, 2, 3, 5]

print("Lista inicial: ",lista)

lista.append(6) #se añande al final de la fila
lista.insert(3, 4) #posicion y valor a agregar
print("Agregar 4 y 6: ",lista)

lista.remove(1) #remover valor
print("Remover el 1 de la lista: ",lista)

lista[0] = 10 #actualizar la posiscion 0 osea el valor (2) por 10
print("Actualizar 2 por 10: ",lista)

indice = lista.index(4) #buscar el valor (4) y arroja la posiscion en la que esta
print("el valor 4 se encuenta en la pocision: ",indice)