
def conversion(x):
        return [10] * (( x // 10 )) + [5] * ((x % 10) //5) + [1] * ((x % 10)%5)
        
    
while True:
    x = int(input())

    if x < 1000 or x > 0:
        print(conversion(x))
        break
    elif x < 0:
        print("Valor no válido")
    else:
        x > 1000
        print("Valor excedido")
  

