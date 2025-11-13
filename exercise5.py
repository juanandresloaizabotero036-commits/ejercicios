def promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3 
    print(f"el promedio es:{promedio: .2f}") 
    
    if promedio >= 3.0:
        print("aprovado")
    else:
        print("resultado: ")
        
        
continuar = True 

while continuar:
    print("calculo promedio de notas")
    n1 = float(input("ingrese la primera nota:"))
    n2 = float(input("ingrese la segunda nota:"))
    n3 = float (input("ingrese la tercera nota:"))
    
    promedio(n1, n2, n3)
    
    respuesta = input("desea ingresar otro estudiante? s/n").lower()
    continuar = (respuesta == "S")

print ("programa finalizado. gracias por usar el sistema.")