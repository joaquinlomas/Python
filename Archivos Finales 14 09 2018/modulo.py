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
    frases=guion.split('\n')                                                    # Lista que guarda lineas de guion separados por \n
    frases_sin_vacios=filter(None,frases)                                       # Es necesario quitar los espacios en blancos de la lista frases.

    lista_interaccion = []                                                      # Lista de personajes que interactuan con el personaje argumento.
    identificador = '-' + personaje                                             # Identificador de personaje argumento (En la lista de frases)

    for i in range(len(frases_sin_vacios)):                                     # I va desde 0 hasta el numero de lineas de frases sin vacios.
        if frases_sin_vacios[i].startswith(identificador):                      # Si la frase actual empieza con nuestro personaje argumento,
            if frases_sin_vacios[i-1].split(':')[0] != identificador and frases_sin_vacios[i-1].startswith('-'): # y si la frase anterior es de otro personaje,                          
                lista_interaccion.append(frases_sin_vacios[i-1].split(':')[0])                                   # Agrega este personaje de la linea anterior a la lista de interaccion.
            if frases_sin_vacios[i+1].split(':')[0] != identificador and frases_sin_vacios[i+1].startswith('-'): # y si la frase siguiente es de otro personaje,
                lista_interaccion.append(frases_sin_vacios[i+1].split(':')[0])                                   # Agrega este personaje de la linea siguiente a la lista de interaccion.
    lista_interaccion=[s.replace('-', '') for s in lista_interaccion]           # Quita los guiones del principio de la lista de personajes relacionados al personaje argumento.
    lista_interaccion = list(set(lista_interaccion))                            # Quita personajes repetidos.
    return lista_interaccion                                                    # Retorna lista de interaccion.
#------------------------------------------------------------------------------------

