# -*- coding: utf-8 -*-

def leer_archivo(nombre = "guion.txt"):
    #entrada: nombre archivo
    #salida: string
    #guion.txt y modulo.py deben estar en el mismo directorio de su script
    with open(nombre, "r") as a:
        return a.read()
        
#Para usar la funcion, puede utilizar la siguiente linea de codigo en su script
#string = leer_archivo()

def dialogos(personaje, guion):
	aux_txt = guion.splitlines()
	txt = []
	interaccion = []

	for j in range(0,len(aux_txt)):			#ciclo for para eliminar las componentes vacias de la lista dado que al comparar los dialogos tienen que estar seguidos 
		if(len(aux_txt[j]) != 0):			#si el elemento de la lista aux_txt contiene algo
			txt.append(aux_txt[j])			#se agrega este a la lista txt que se analizara

	for i in range(0,len(txt)):
		aux = txt[i]						#linea actual
		if(i==0):
			if(aux[0]=='-'):
				aux_list = aux[1:len(aux)-1].split(":")
				if(aux_list[0]==personaje):
					aux_str1 = txt[i+1].split(":")
					if(aux_str1[0] == personaje):
						interaccion.append(aux_str1)
		elif(i==len(txt)-1):
			if(aux[0]=='-'):
				aux_list = aux[1:len(aux)-1].split(":")
				if(aux_list[0]==personaje):
					aux_str1 = txt[i-1].split(":")
					if(aux_str1[0] == personaje):
						interaccion.append(aux_str1)
		else:
			if(aux[0]=='-'):
				aux_list = aux[1:len(aux)-1].split(":")
				if(aux_list[0]==personaje):
					aux_str1 = txt[i-1]
					aux_str2 = txt[i+1]
					if(aux_str1[0]=='-'):
						aux_str1 = aux_str1[1:len(aux_str1)-1].split(":")
						interaccion.append(aux_str1[0])
					if(aux_str2[0]=='-'):
						aux_str2 = aux_str2[1:len(aux_str2)-1].split(":")
						interaccion.append(aux_str2[0])
	return list(set(interaccion))