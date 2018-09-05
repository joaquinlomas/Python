from modulo import leer_archivo

guion = leer_archivo('guion2.txt')		#lectura desde archivo                                            #Lista para reemplazo
lineas = guion.split('\n')
lineas_personajes = []
for i in lineas:                                  #Guardamos en la lista personajes solamente aquellos de la lista filtrado que empiecen con un guion
    if i.startswith('-'):
        lineas_personajes.append(i)
#print lineas_personajes
lista_personajes = [i.split(':')[0] for i in lineas_personajes]
#print lista_personajes
personajes = list(set(lista_personajes))
#print personajes
personajes_principales = [i.replace('-','') for i in personajes]
#print personajes_principales
dialogos = [i.split(':')[1] for i in lineas_personajes]
d = {}
lista = []
for z in personajes:
	for i in xrange(len(lineas_personajes)):
		aux = lineas_personajes[i]
		if aux.startswith(z):
			lista.append(dialogos[i]) 
	d[z] = lista
#print d
