#-------------------------------------------------------------------------------
# Definir una lista de números
#Mostrar por pantalla el valor promedio de la lista.
#No utilizar funciones sum ni len
#-------------------------------------------------------------------------------

def main():
    pass

    listnro = [10,20,30]
    contador= 0
    suma= 0

    for i in listnro:
        contador=contador + 1

    for i in listnro:
        suma = suma + i

    promedio = suma / contador

    print (f'El promedio es {promedio}')



if __name__ == '__main__':
    main()
