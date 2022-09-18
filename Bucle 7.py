#-------------------------------------------------------------------------------
# Definir una lista de números
#Encontrar el valor máximo de la lista
#Imprimir el valor
#No utilizar max
#-------------------------------------------------------------------------------

def main():
    pass

    lista= [85,5,8,12,86,74,56,100,1000,2000,3000,5000]
    valormax= 0

    for i in range (0, len (lista)):
        if lista [i] > valormax:
            valormax = lista [i]

    print( valormax)


if __name__ == '__main__':
    main()
