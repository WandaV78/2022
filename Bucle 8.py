#-------------------------------------------------------------------------------
#Definir una lista de números
#Encontrar el valor mínimo de la lista
#Imprimir el valor
#No utilizar mi
#-------------------------------------------------------------------------------

def main():
    pass

    lista = [50,45,89,43,12,5, 1]
    nromin = 9999999999

    for i in range (0, len (lista)):
        if lista [i] < nromin:
            nromin = lista [i]

    print (f'El numero minimo de la lista es {nromin}')

if __name__ == '__main__':
    main()
