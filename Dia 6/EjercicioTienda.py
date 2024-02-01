# --------------------------------------------------
# ------------   Tienda gamer   --------------------
# --------------------------------------------------

Tienda = {'Teclado':50000,'Mouse':20000,'Audifonos':70000,'Cables USB':20000}

print('Bienvenido a la tienda gamer')
print('los productos en stock son los siguientes: ')
print(Tienda)

prod = str(input('ingrese el nombre del producto a comprar: '))

if prod == 'Teclado' or 'teclado' or 'teclados':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print(Tienda['Teclado']* cant) 
    print('Gracias por su compra de Teclado, que tenga un buen dia')

elif prod == 'Mouse' or 'mouse' or 'raton' or 'ratones':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print(Tienda['Mouse']* cant) 
    print('Gracias por su compra de Mouse Gamer, que tenga un buen dia')

elif prod == 'Audifonos' or 'Audífonos' or 'audifonos' or 'audífonos' or 'diadema' or 'diadema gamer':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print(Tienda['Audifonos']* cant) 
    print('Gracias por su compra de Audifonos gamer, que tenga un buen dia')

elif prod == 'Cables usb' or 'Cables USB' or 'cables usb' or 'cables':
    cant = int(input('ingrese la cantidad a comprar: '))
    print('el total de su compra es de: ')
    print (Tienda['Cables USB']* cant) 
    print('Gracias por su compra de Cables para su ordenador, que tenga un buen dia')

else:
    print('Actualmente no contamos con stock para el producto ', prod, ', vuelva después para revisarlo.')
    