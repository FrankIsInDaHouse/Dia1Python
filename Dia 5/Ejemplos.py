diccionario = {'nombre':'Esparza','Edad':19,'Barrio':'Cataluña'}
print(diccionario)
print(type(diccionario))

diccionario['nombre']= str(input('Ingrese su nombre: '))
print ('bienvenido, ', diccionario['nombre'])

diccionario['Edad'] = int(input('Ingrese su edad: '))
print ('su edad es' , diccionario['Edad'], 'años')

diccionario['Barrio'] = str(input('ingrese su zona de residencia: '))
print('su zona de residencia es ', diccionario['Barrio'])

#clear = limpiar una lista (lista.clear())
diccionario.clear()
print (diccionario)



# eliminar una llave o dato de una lista = lista.popitem()
diccionario.pop('nombre','Esparza')
print (diccionario)
print('')

# actualizar una lista con otra = .update

diccionario2 = {'nombre':'Sebas','Edad':'20','Barrio':'Villamil'}
diccionario.update(diccionario2)
print(diccionario)
















