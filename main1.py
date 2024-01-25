##-------------------------------------------------------
##--------          Ejercicio 1        ------------------
##-------------------------------------------------------
##Impresión en consola
print ("hola mundo")

##-----------------    Datos primitivos     --------------
##String
texto = "Campus"
print(texto)
print(type(texto))
##Int
numeroEntero = 1
print(numeroEntero)
##Float
numeroDecimal = 3.1
print(numeroDecimal)
##Double
numeroDecimalLargo = 3.14159
print(numeroDecimalLargo)
##Boolean
booleano = True
print(booleano)

##----------      Entradas parte del usuario     ---------
entradaUsuario = input("ingresa tu nombre: ")
print("Tu nombre es: ", entradaUsuario)

#----------      Entradas parte del usuario con definición de tipo de dato primitivo     ---------

entradaUsuarioNumero = input("ingresa tu edad: ")
numeroFinal = int(entradaUsuarioNumero) #nombre de la variable = tipo de dato(nombre del dato anterior)
print("Tu edad es: ", numeroFinal)

##-----------            ciclo "for"         -----------------------
##Ciclo "for"
for i in range (5,20,3): #for "contador, osea i" in range (desde,hasta,pasos)
    print(i+1) # imprime el resultado especificado en la linea anterior

##---------------------         ciclo while      ---------------------
booleanito = True
while booleanito == True: 
    print("Sigo vivo tonotos")
    booleanito = False

##---------------      condicionales       -----------------------
Texto1 = "campus"
if Texto1 == "campus":
    print("Soy campus tonotos")
else:
    print("no soy campus :c")
##desarrollado por NOMBRE FRANK SEBASTIÁN ESPARZA RIAÑO - 1097789710