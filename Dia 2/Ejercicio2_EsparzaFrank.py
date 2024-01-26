print("")        #Imprime la introducción
print("Bienvenido al algoritmo de adivinanza de un número del 1 al 100")
print("")
print("---------------------------------------------------------------")
print("")


import random # Import sirve para importar variables, contantes, funciones, clases hasta módulos y paquetes. Con el comando importamos el módulo 'Random' con el cual podemos generar números aleatorios a partir de fuentes generadas por el sistema operativo.

def game():   #definimos la función que nos permitirá jugar a adivinar el número.
    number_to_guess = random.randint(1, 100) # Acá usamos el módulo random.randint para generar un número entero aleatorio entre uno y cien. la palabra randint la compone rand de la parte random e int de la parte entero.
    attempts_left = 10 # creamos la variable intentos restantes y la asignamos con 10 principalmente

    print("Adivina el número secreto entre 1 y 100. Tienes 10 intentos.") 

    while attempts_left > 0: # acá declaramos que mientras la variable de intentos restantes sea mayor a cero el juego estará en marcha.
        try:   # equivalente a hacer en pseint
            guess = int(input("Intenta adivinar el número: "))  # acá creamos la variable guess que almacenará los números de intentos digitados del usuario
        except ValueError:   # Except es para ejecutar una serie de instrucciones si try falla, ValueError es por si lo que falla es la variable, en este caso si se intenta digitar una variable que no sea un entero.
            print("Entrada no válida. Por favor, ingresa un número.") # Especificamos que el tipo de variable digitada no es válida
            continue # este comando nos permite omitir la parte anterior del bucle en la que se detecta el ValueError, para seguir con el resto del bucle si todo está bien.

        attempts_left -= 1 # acá se van restando los intentos restantes que tiene el usuario, comenzando desde diez y terminando en cero.

        if guess < number_to_guess:  # acá determinamos si el número que escribe el usuario es menor al número a adivinar imprimirá que el número secreto es mayor al número digitado.
            print("El número secreto es más alto.")
        elif guess > number_to_guess:    # usamos un else if unido, osea un elif, para determinar otra posible situación, en este caso, si el número que escribe el usuario es mayor al número a adivinar imprimirá que el número secreto es menor al número digitado.
            print("El número secreto es más bajo.")
        else: # en else determinamos la situación de victoria
            print(f"¡Felicidades! Adivinaste el número secreto ({number_to_guess}) en {10 - attempts_left} intentos.") #Felicitamos al usuario.
            return #acá usamos return (osea retorno o devolver) para devolver la situación de victoria si el usuario ganó el juego.

    print(f"Lo siento, no adivinaste el número secreto ({number_to_guess}). Se acabaron tus intentos.") #Acá imprimimos el resultado en caso de que el usuario haya perdido el juego.

if __name__ == "__main__":
    game()