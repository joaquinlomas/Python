# -*- coding: utf-8 -*-

from modulo import *

guion = leer_archivo("guion2.txt")					#guion es un string largo que contiene el txt

lineas  = guion.splitlines()					#lista que cada componente es una parte del guion hasta un salto de linea
dialogo = []									#lista vacia que contiene todos los string de dialogos
nombres = []									#lista vacia que contendra solo los nombres de los personajes

#EJERCICIO A)
for i in lineas:
	if((len(i) != 0) and (i[0] == '-')):			#condicion para filtrar los dialogos de otras cosas redactadas en el guion, los dialogos SIEMPRE empiezan con '-'
		dialogo.append(i[1:len(i)-1])				#agrega los string de dialogos sin contar el primer elemento '-' a la lista dialogos
for j in dialogo:
	aux = j.split(":")								#separa los nombres de los personajes a partir de ':', aux pasa a ser una lista de 3 elementos. 'nombre'+':'+'dialogo'
	nombres.append(aux[0])							#agrega el primer elemento de la lista (el nombre del personaje) a la lista nombres

nombres = list(set(nombres))						#set() crea un conjunto que elimina los elementos repetidos

#EJERCICIO B)
diccionario            = {}							#diccionario con los nombres (key) y dialogos (value)
diccionario_dialogos   = {}							#diccionario con los nombres (key) y numero de dialogos (value)
diccionario_l_dialogos = {}							#diccionario con los nombres (key) y largo mas grande de los dialogos (value)
for x in nombres:									#recorre todos los personajes
	auxdia = []										#crea una lista vacia para guardar los dialogos
	for y in dialogo:								#recorre todos los dialogos			
		aux1 = y.split(":")							#separa los dialogos en personajes-dialogo y los guarda en una lista
		if((len(aux1) == 2) and (x == aux1[0])):	#condicion: la longitud del vector de dialogos debe ser de 2 y la primera componente igual al valor x que esta recorriendo el for
			auxdia.append(aux1[1])					#agrega el dialogo del personaje a un vector auxiliar
		if((len(aux1) == 3) and (x == aux1[0])):
			auxdia.append(aux1[1] + aux1[2])		#es el caso cuando hay interacciones del autor o cuando el personaje cita algo porque aparecen denuevo los : 
	diccionario[x] = auxdia							#relaciona todos los dialogos con el personaje x en un diccionario
	diccionario_dialogos[x] = len(auxdia)			#diccionario con los personajes y el numero de dialogos que tiene (para la c) )

#EJERCICIO C)
diccionario_n_max = {}
diccionario_n_min = {}
for a in diccionario.keys():
	num   = []
	for b in diccionario[a]:
		num.append(len(b.split()))
	diccionario_n_min[a] = min(num)
	diccionario_n_max[a] = max(num)

diccionario_n_max = diccionario_n_max.items()
diccionario_n_min = diccionario_n_min.items()
diccionario_n_max.sort(key=lambda z: z[1])
diccionario_n_min.sort(key=lambda z: z[1])
print "C.1)" + '\n' + "Personaje con el dialogo mas extenso: " + str(diccionario_n_max[len(diccionario_n_max)-1]) + '\n' + "Personaje con el dialogo menos extenso: " + str(diccionario_n_min)
diccionario_dialogos = diccionario_dialogos.items()	#.items() convierte un diccionario a una lista de tuplas
diccionario_dialogos.sort(key=lambda z: z[1])		#key(cable) es el criterio de orden y la funcion lambda es para acceder a la segunda componente de la tupla (numero de dialogos) y ordenar la lista por este parametro
print "C.2)" + '\n' + "Personaje con menos dialogos: " + str(diccionario_dialogos[0]) + '\n' + "Personaje con mas dialogos: " + str(diccionario_dialogos[len(diccionario_dialogos)-1])

#EJERCICIO D)
print '\n' + '\n' + '\n' + '\n' + '\n'
print "D)"
ejemplo = dialogos(nombres[15],guion)
print nombres[15]
print ejemplo