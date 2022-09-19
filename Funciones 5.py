#-------------------------------------------------------------------------------
'''
Realizar una función que se llame recortar() que reciba 3 parámetros.
1º param => nro a recortar
2º param => es el límite inferior
3º param => es el límite superior
La función debe cumplir lo siguiente:
Devolver el límite inferior si el nro es menor
Devolver el límite superior si el nro es mayor
Devolver el nro si no supera los límites
'''
#-------------------------------------------------------------------------------
def recortar (nrorecortar,limiteinf=2,limitesup=4):
    if (nrorecortar < limiteinf):
        return (limiteinf)
    elif (nrorecortar > limitesup):
        return (limitesup)
    else:
        return nrorecortar

print (recortar (3))


