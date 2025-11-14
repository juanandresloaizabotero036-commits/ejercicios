productos = []

continuar = "si"
while continuar.lower () == "si":
    nombre =  input("ingrese el nombre del producto:")
    
    
    while True:
        try:
            precio = float(input("ingrese el precio del producto:"))
            break 
        except ValueError:
            print( "debe ingresar un numero entero valido")
            
    while True:
        try:
            cantidad = int(input("ingresa la cantidad de producto"))
            break
        except ValueError:
            print ("debe ingresa un numero entero valido")
    
    
    totalinventario = precio * cantidad
    print("Total por este producto:", totalinventario)
            
    producto = {
        "nombre": nombre,
        "precio" : precio,
        "cantidad" : cantidad,
        "totalinventario": totalinventario
    }
    productos.append(producto) 
    
    
    continuar = input("¿Desea registrar otro producto? (si/no): ")

print("\n--- REPORTE DE PRODUCTOS ---")
for p in productos:
    print(f"Nombre: {p['nombre']}, Precio: {p['precio']}, "
        f"Cantidad: {p['cantidad']}, Total: {p['totalinventario']}")
    
print("\nCantidad total de productos registrados:", len(productos))
