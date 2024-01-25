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
for i in range (1,20,2): #for "contador, osea i" in range (desde,hasta,pasos)
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


## ----------------         Funciones       ----------------------


## -----------    funcion con retorno con parámetros     ---------------------

def sumita (a, b):      ## def(comando para iniciar una funcion), nombre funcion, (parámetros)
    return a + b        ## return es el comando para retornar un valor

result = sumita(1, 2)
print(result)

#-------------    función sin retorno sin parámetros     ---------------------

def saludo():
    print("Hola invitado")

saludo()

# ------------    función sin retorno con parámetros     ---------------------

def saludoNombre(name):
    print ("Hola usuario/a " + name + "!" )

name = input ("ingrese su nombre: ")

saludoNombre(name)

# ------------    función con retorno sin parámetros     ---------------------

def resultado():
    resultadito = a + b
    return resultadito

a = float(input("Digite el primer número de la suma: "))
b = float(input("digite el segundo número de la suma: "))

print("El resultado de la suma es ", resultado())

# ------------    Arreglos      ---------------------

Lista = [1,2,3,4,5]

print("Lista de números del 1 al 5")
print("")
print(Lista[0])
print(Lista[1])
print(Lista[2])
print(Lista[3])
print(Lista[4])


##desarrollado por NOMBRE FRANK SEBASTIÁN ESPARZA RIAÑO - 1097789710