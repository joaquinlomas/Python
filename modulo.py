# -*- coding: utf-8 -*-

def leer_archivo(nombre = "guion.txt"):
    #entrada: nombre archivo
    #salida: string
    #guion.txt y modulo.py deben estar en el mismo directorio de su script
    with open(nombre, "r") as a:
        return a.read()
        
#Para usar la funcion, puede utilizar la siguiente linea de codigo en su script
#string = leer_archivo()
        
#------------------------------------------------------------------------------------------------------------------------------------------------

# d) Crear una funcion que reciba un personaje y el guion y retorne una lista con los nombres de los personajes con los cuales interactua.

def interactua_con (personaje, guion):

    guion=leer_archivo(guion)                                                   # Lectura desde archivo.
    lista=[]                                                      # Lista para reemplazo.
    frases=guion.split('\n')                                      # Separamos el string separando por nueva linea.
    
    for j in frases:                                           # Guardamos en la lista personajes solamente aquellos de la lista filtrado que empiecen con un guion.
        if j.startswith('-'):
            lista.append(j)
    lista_interaccion = []                                                        # Lista de personajes que interactuan con el personaje argumento.
    identificador = '-' + personaje                                                 # Identificador de personaje argumento (En la lista de frases)

    for i in range(len(lista)):
        if lista[i].startswith(identificador):
            if lista[i-1].split(':')[0] != identificador:
                lista_interaccion.append(lista[i-1].split(':')[0])
            if lista[i+1].split(':')[0] != identificador:
                lista_interaccion.append(lista[i+1].split(':')[0])
    lista_interaccion=[s.replace('-', '') for s in lista_interaccion]           # Quita los guiones del principio de la lista de personajes relacionados al personaje argumento.
    lista_interaccion = list(set(lista_interaccion))
    return lista_interaccion
#------------------------------------------------------------------------------------
