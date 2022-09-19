#-------------------------------------------------------------------------------
'''
Realizar una función que se llame relacion() que a partir de dos nros realicce
lo siguiente:
Si el primer nro es mayor que el segundo, devuelva 1
Si el primer nro es menor que el segundo, devuelva -1
Si ambos nros son iguales, devuelva 0
'''
#-------------------------------------------------------------------------------

def relacion( nro1, nro2):
        if (nro1 > nro2):
            return 1
        elif (nro1 < nro2):
            return -1
        else :
            return 0


print (relacion (2,9))
