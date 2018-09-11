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
    frases=guion.split('\n')                                                    # Separamos el string separando por nueva linea.
    frases_sin_vacios=filter(None,frases)                                       # Es necesario quitar los espacios en blancos de la lista frases.

    lista_interaccion=[]                                                        # Lista de personajes que interactuan con el personaje argumento.
    frase_pasada=''                                                             # Buffer para guardar frase anterior a la actual en ciclo for.
    identificador='-'+personaje                                                 # Identificador de personaje argumento (En la lista de frases)

    for k in frases_sin_vacios:
        if k.startswith('-') and frase_pasada.startswith(identificador):        # Si la frase empieza con guion y la frase anterior es un dialogo del personaje objetivo
            lista_interaccion.append(k.split(':')[0])                           # Guarda el personaje con el que hablo.     
        frase_pasada=k                                                          # Ademas, guarda la frase actual en el buffer para la siguiente iteracion.

    lista_interaccion=[s.replace('-', '') for s in lista_interaccion]           # Quita los guiones del principio de la lista de personajes relacionados al personaje argumento.
    lista_interaccion=list(set(lista_interaccion))                              # Limpieza de personajes repetidos.
    
    return lista_interaccion                                                    # La funcion retorna la lista de personajes que interactuan con el personaje argumento.

#------------------------------------------------------------------------------------
