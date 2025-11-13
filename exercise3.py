preciou = float(input("ingrese preciou:"))

if preciou >= 50000:
    descuento = preciou *0.10
    preciofinal = descuento - preciou
    
print ( "descuento", round (descuento,2))
print ( "preciofinal", round (preciofinal,2))