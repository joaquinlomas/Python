from modulo import leer_archivo

guion=leer_archivo('guion2.txt')                    #Lectura desde archivo
lista=[]                                            #Lista para reemplazo
palabras=guion.split('\n')                          #Separamos el string separando por nueva linea
filtrado = [i.split(':')[0] for i in palabras]      #Separar todo los strings por los ":" y guardar el primer string en la lista    
for j in filtrado:                                  #Guardamos en la lista personajes solamente aquellos de la lista filtrado que empiecen con un guion
    if j.startswith('-'):
        lista.append(j)
filtrado2=list(set(lista))                         #Limpieza de personajes repetidos
lista_personajes=[s.replace('-', '') for s in filtrado2] #Quita los guiones del principio

# b) Crear un diccionario que asocie cada personaje con sus respectivos diaogos en la forma:
# {personaje1:[dialogo1,dialogo2,...],personaje2:[dialogo1,dialogo2,...],..}

diccionario = {}
for n in filtrado2:
    diccionario.append(n)
    for k in palabras:
        if k.startswith(n):
            diccionario[n] = append(k.split(':'))
            
            
    

#if palabras.startswitch(-NOMBRE_PERSONAJE)
#   diccionario.append(palabras)


# c) contar la cantidad de veces que habla cada personaje contando cada aparicion en filtrado2
