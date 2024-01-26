## -------------      Serie de Fibonacci       ----------------

def fibonacci(n):  #definimos la función llamada Fibonacci
    datosPrimarios = [0, 1]
    while len(datosPrimarios) < n:
        datosPrimarios.append(datosPrimarios[-1] + datosPrimarios[-2])
    return datosPrimarios

print("")
print("Bienvenido al algoritmo Seire de Fibonacci")
print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")
print("La serie Fibonacci es un conjunto de números enteros los cuales ascienden desde 0 infinitamente.")
print("")
print("Lo que distingue a la serie Fibonacci de cualquier otro grupo de números es que su forma de ascender es en base a la suma.")
print("el número inicial de la serie Fibonacci es cero '0', el segundo número es uno '1', el tercer número es el resultado de la suma de estos dos números, osea uno '1'.")
print("Entonces ¿Cómo se sigue la serie de Fibonacci? Muy fácil. Para determinar los valores se toma la suma base(la cual es 0+1=1) y se extrae el valor del segundo número de la suma y del resultado")
print("una vez con estos valores, solamente los sumamos, en este caso seria (1+1=2), por lo que el cuarto valor de la serie Fibonacci sería 2.")
print("Para seguir sacando los valores posteriores dejamos de lado la suma base, y pasamos a simplemente tomar la suma anterior (en este caso 1+1=2) y hacemos el mismo proceso (1+2=3, 2+3=5, 3+5=8, Etc.)")
print("")
print("repetimos el proceso el número de veces que el usuario decida.")
print("")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print ("")

while True: #while True ejecuta el programa infinitas veces, ya que True es verdadero, y no hay nada que lo haga ser falso, osea False.
    try: #Try es el equivalente a Hacer en pseint.
        n = int(input("Ingrese el número de valores de la serie que desea ver: "))    #definimos la variable aqui.
        if n < 0:     # aqui condicionamos la variable n, si es menor a cero imprimirá el siguiente texto 
            print("No puede ser un número negativo. Por favor, ingrese un número positivo")   #texto a inprimir si n es menor a cero.
        else:     #else es el equivalente al SiNo de pseint
            break  #este comando permite detener el ciclo while (mientras) si se rompe una condicion externa al if, en este caso, si se digita algun carácter que no sea un número entero.
    except ValueError: #este comando se ejecuta si el comando try falla, nos permite ejecutar una serie de instrucciones para aclarar cual fué el fallo.
        print("Caracteres no válidos. Por favor, ingrese solo números") # dentro de except ponemos algo para aclarar el fallo, ValueError sirve para aclarar que el error fue de tipo variable (poner un tipo de variable que no concuerda con el asignado anteriormente)

while n != 0: #la condicion si n es diferente a cero, solo puede ser positivo ya que anteriormente lo condicionamos para no ser negativo, y no puede ser de otro tipo de variable porque lo lanzará como error
    secuencia = fibonacci(n) #aqui asignamos la función fibonacci con el nombre de secuencia
    print(secuencia) #imprimimos la serie fibonacci con el nombre asignado secuencia
    while True: #lo ejecutará infinitamente mientras la condición sea verdad (while True) 
        try: # equivalente a Hacer en pseint
            n = int(input("Ingrese un número de valores de la serie que quiera ver (si desea terminar el algoritmo, presione cero '0') ")) # pide que ingrese un nuevo número que sera el número de valores a imprimir, o si quiere terminar el programa presionando cero.
            if n < 0: #lo mismo que en el primer bloque de código.
                print("No puede ser un número negativo, ingrese un número positivo")
            else:
                break
        except ValueError:
            print("Caracteres no válidos. Por favor, ingrese solo números")

print("")
print("----------------------------------------------------------")
print("")
print("gracias por usar el algoritmo, tenga un buen dia :)")
print("")

## Algoritmo hecho por FRANK SEBASTIÁN ESPARZA RIAÑO - 1097789710





