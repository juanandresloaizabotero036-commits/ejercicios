while True:
    nombre = str(input("Ingresa el nombre del producto: "))
 
    # aqui validamos que el registro ingresado sea correcto y nos arroje el dato si el registro es un codigo erroneo
    while True:
        try:
            precio = float(input("Ingresa el precio del producto: "))
            break
        except ValueError:
            print("Error en  el precio.")

    # aqui intentamos validar cantidad sea verdadera si no lo es entonces mostrar que es un codigo erroneo
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad deseada: "))
            break
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

    #por ultimo calculamos el costo total del producto
    costo_total = precio * cantidad

    print("Nombre:", nombre)
    print("Precio:", precio)
    print("Cantidad:", cantidad)
    print("Costo total:", costo_total)

    break