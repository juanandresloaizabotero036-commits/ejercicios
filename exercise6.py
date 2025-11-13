num_pasajeros = int(input("Ingresa el número de pasajeros: "))
for i in range (1, numpasajero + 1):
    if i == 10:
        print("bus lleno")
        break
    else: 
        print(f"pasajero {i} a abordo:")