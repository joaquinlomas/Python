
#                                                Tarea N°1 Python Cientifico
#                                               Joaquin Lomas y Matias Pereira
#
# a) Crear una lista de strings sin elementos repetidos que contenga todos los nombres de los personajes
#    principales del texto, estos tienen el formato -NOMBRE_PERSONAJE:

from modulo import leer_archivo,interactua_con

import operator                                               # Utilizado en Parte C.1

guion=leer_archivo('guion2.txt')                              # Lectura desde archivo.
lista=[]                                                      # Lista para reemplazo.
frases=guion.split('\n')                                      # Separamos el string separando por nueva linea.
filtrado1 = [i.split(':')[0] for i in frases]                 # Separar todo los strings por los ":" y guardar el primer string en la lista.    
for j in filtrado1:                                           # Guardamos en la lista personajes solamente aquellos de la lista filtrado que empiecen con un guion.
    if j.startswith('-'):
        lista.append(j)
filtrado2=list(set(lista))                                    # Limpieza de personajes repetidos.
lista_personajes=[s.replace('-', '') for s in filtrado2]      # Quita los guiones del principio y la lista de personajes principales se guarda en lista_personajes

# ------------------------------------------------------------------------------------------------------------------
# b) Crear un diccionario que asocie cada personaje con sus respectivos diaogos en la forma:
# {personaje1:[dialogo1,dialogo2,...],personaje2:[dialogo1,dialogo2,...],..}

lista2=[]                                                     # Lista2 guarda solamente los dialogos de los personajes.
for j in frases:             
    if j.startswith('-'):
        lista2.append(j)

dialogos_conguion=[]                                          # Lista de listas que guarda dialogos de cada personaje.
for j in filtrado2:                                           # Recorre lista de personajes.
    for i in range(len(lista2)):
        if lista2[i].startswith(j):
            dialogos_conguion.append(lista2[i])

dialogos=[s.replace('-', '') for s in dialogos_conguion]     # Quita los guiones del principio de dialogos_conguion
diccionario = dict([i, 0] for i in lista_personajes)         # Generacion de diccionario

for k in diccionario.keys():                                 # El valor de cada key del diccionario (Personajes) ahora sera una lista (Que almacenara los dialogos de cada uno)
    diccionario[k]=[]                                        

for k in diccionario.keys():                                 # Itera personaje por personaje
    for i in dialogos:                                       # Itera por todo el dialogo, donde estan incluidos los dialogos de todos los personajes.
        if i.startswith(k):                                  # Si la linea de dialogo empieza con el nombre de un personaje, 
            diccionario[k].append(i)                         # entonces agrega esa linea de dialogo a la lista de ese personaje en el diccionario

for k in diccionario.keys():
    diccionario[k]=[i.split(':')[1] for i in diccionario[k]] # Los dialogos se guardaron en cada lista pero mantienen la forma 
                                                             # PERSONAJE: DIALOGO... entonces debemos recortar "PERSONAJE:" con split
# -------------------------------------------------------------------------------------------------------------------------
#
# c) Responder a las siguientes preguntas:
#    c.1) que personaje tiene el dialogo mas y menos extenso? (numero de palabras)
#    c.2) Que personaje tiene mas y menos dialogos?

# C.1 
contador = dict([i, 0] for i in diccionario.keys())         # Generacion de diccionario
for k in contador.keys():                                   # El valor de cada key del diccionario (Personajes) ahora sera una lista (Que almacenara los dialogos de cada uno)
    contador[k]=[]

for k in diccionario.keys() :                               # Para cada personaje del diccionario
    for j in diccionario[k]:                                # Para cada dialogo de un personaje
        contador[k].append(len(j.split()))                  # Guarda en la lista de contador de cada personaje la cantidad de palabras de cada dialogo, 
                                                            # en este caso split se usa para contar las palabras.

numero_palabras_max = dict([i, 0] for i in diccionario.keys())  # Generacion de diccionario de cantidad de palabras del dialogo mas largo de cada personaje.
numero_palabras_min = dict([i, 0] for i in diccionario.keys())  # Generacion de diccionario de cantidad de palabras del dialogo mas corto de cada personaje.

for k in contador.keys():                                   # Por cada key de contador (lista de personajes),
    numero_palabras_max[k]=max(contador[k])                 # suma la cantidad de paralabras totales de cada uno y guardalo en la lista numero_palabras.
    numero_palabras_min[k]=min(contador[k])                 # suma la cantidad de paralabras totales de cada uno y guardalo en la lista numero_palabras.


dialogo_mas_extenso=max(numero_palabras_max.iteritems(), key=operator.itemgetter(1))[0]   # Funcion lee todo el diccionario y entrega el key (personaje) 
                                                                                      # donde este el value mayor (El que tenga el dialogo mas largo segun cant de palabras).
dialogo_menos_extenso=min(numero_palabras_min.iteritems(), key=operator.itemgetter(1))[0] # Funcion lee todo el diccionario y entrega el key (personaje) 
                                                                                      # el value menor (El que tenga el dialogo mas corto segun cantidad de palabras).

print "C.1" 
print "Personaje con dialogo mas extenso:%s" % (dialogo_mas_extenso)             # Impresión de personaje con dialogo mas extenso.
print "Personaje con dialogo menos extenso:%s" % (dialogo_menos_extenso)         # Impresion de personaje con dialogo mas corto.


# C.2
largo_dialogos=[]                                           # Genera lista que almacenara la cantidad de dialogos de cada personaje
for k in diccionario.keys() :                               # Para cada uno de los personajes, se almacena la cantidad de dialogos que tienen
    largo_dialogos.append(len(diccionario[k]))              # (solo la cantidad de dialogos, no se especifica cual personaje hizo que cantidad de dialogos)
                                                            
dialogo_max=max(largo_dialogos)                             # La funcion max encuentra el valor maximo de la lista, es decir la cantidad de dialogos del personaje que hablo mas.
dialogo_min=min(largo_dialogos)                             # La funcion min encuentra el valor minimo de la lista, es decir la cantidad de dialogos del personaje que hablo menos.

for k in diccionario.keys() :                               # Para cada uno de los personajes de la lista,
    if len(diccionario[k])==dialogo_max:                    # aquel cuya cantidad de dialogos sea igual a la dialogo_max
        dialogador_max=k                                    # es aquel personaje con la mayor cantidad de dialogos, el cual se guarda en dialogador_max
    if len(diccionario[k])==dialogo_min:                    # y aquel cuya cantidad de dialogos sea igual a la dialogo_min                 
        dialogador_min=k                                    # es aquel personaje con la menor cantidad de dialogos, el cual se guarda en dialogador_min

print "C.2" 
print "Personaje con mayor cantidad de dialogos:%s" % (dialogador_max)         # Impresion de personaje con mayor cantidad de dialogos. (El que habla mas veces)
print "Personaje con menor cantidad de dialogos:%s" % (dialogador_min)         # Impresion de personaje con menor cantidad de dialogos. (El que habla menos veces)

#----------------------------------------------------------------------------------------------------------------------------------------------------

# d) Se encuentra en archivo modulo.py

interactuan_con_tony=interactua_con('TONY','guion2.txt')

interactuan_con_loki=interactua_con('LOKI','guion2.txt')

print interactuan_con_tony

print interactuan_con_loki












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

