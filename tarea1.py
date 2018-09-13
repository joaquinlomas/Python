# -*- coding: utf-8 -*-
#                                              Tarea N°1 Python Cientifico
#                                               Joaquin Lomas y Matias Pereira
#
# a) Crear una lista de strings sin elementos repetidos que contenga todos los nombres de los personajes
#    principales del texto, estos tienen el formato -NOMBRE_PERSONAJE:

from modulo import leer_archivo,interactua_con

import operator                                               # Utilizado en Parte C.1

guion=leer_archivo('guion2.txt')                              # Lectura desde archivo.
lista=[]                                                      # Lista para reemplazo.
frases=guion.split('\n')                                      # Separamos el string separando por nueva linea.
for j in frases:                                           # Guardamos en la lista personajes solamente aquellos de la lista filtrado que empiecen con un guion.
    if j.startswith('-'):
        lista.append(j)
filtrado = list(set([i.split(':')[0] for i in lista] ))                                    # Limpieza de personajes repetidos.
lista_personajes = [s.replace('-', '') for s in filtrado]     # Quita los guiones del principio y la lista de personajes principales se guarda en lista_personajes
diccionario = dict([i, 0] for i in lista_personajes)         # Generacion de diccionario
for k in diccionario.keys():                                 # El valor de cada key del diccionario (Personajes) ahora sera una lista (Que almacenara los dialogos de cada uno)
    diccionario[k]=[]                                        
for k in filtrado:                                 # Itera personaje por personaje
    for i in lista:                                       # Itera por todo el dialogo, donde estan incluidos los dialogos de todos los personajes.
        aux = i.split(':')[1]
        if i.startswith(k):                                  # Si la linea de dialogo empieza con el nombre de un personaje, 
            if aux.startswith(' '):
                diccionario[k.replace('-','')].append(aux)                         # entonces agrega esa linea de dialogo a la lista de ese personaje en el diccionario
#print diccionario
# -------------------------------------------------------------------------------------------------------------------------
# c) Responder a las siguientes preguntas:
#    c.1) que personaje tiene el dialogo mas y menos extenso? (numero de palabras)
#    c.2) Que personaje tiene mas y menos dialogos?

# C.1 
contador = dict([i, 0] for i in diccionario.keys())         # Generacion de diccionario
for k in contador.keys():                                   # El valor de cada key del diccionario (Personajes) ahora sera una lista (Que almacenara los dialogos de cada uno)
    contador[k]=[]

for k in diccionario.keys():
    aux = []                               # Para cada personaje del diccionario
    for j in diccionario[k]:                                # Para cada dialogo de un personaje
        aux.append(len(j.split()))                  # Guarda en la lista de contador de cada personaje la cantidad de palabras de cada dialogo, 
    contador[k] = [max(aux),min(aux)]                                                        # en este caso split se usa para contar las palabras.
print contador
maximo = max(contador[k][0] for k in contador.keys())
minimo = min(contador[k][1] for k in contador.keys())
dialogo_max = []
dialogo_min = []
for k in contador.keys():
    if contador[k][0] == maximo:
        dialogo_max.append(k)
    if contador[k][1] == minimo:
        dialogo_min.append(k)

print('El personaje con el dialogo mas largo es ' + str(dialogo_max))
print('Los personajes con el dialogo mas corto son ' + str(dialogo_min))

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
print('El personaje con mayor cantidad de dialogos es ' + dialogador_max + ' con ' + str(dialogo_max))         # Impresion de personaje con mayor cantidad de dialogos. (El que habla mas veces)
print('El personaje con menor cantidad de dialogos es ' + dialogador_min + ' con ' + str(dialogo_min))         # Impresion de personaje con menor cantidad de dialogos. (El que habla menos veces)

#----------------------------------------------------------------------------------------------------------------------------------------------------

# d) Se encuentra en archivo modulo.py
personaje = input('Introduzca el nombre de un personaje: ')

interactua_con_personaje=interactua_con(personaje,'guion2.txt')

print interactuan_con_personaje












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

