#-------------------------------------------------------------------------------
'''
Pedir al usuario que ingrese dos nros
Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
Pedir al usuario que ingrese una opción
Verificar la opción del usuario
Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
ingrese una opción
Ejecutar la operación
Mostrar por pantalla el resultado
'''
#-------------------------------------------------------------------------------

def main():
    pass

    nro1 = int (input ("Ingrese un nro"))
    nro2 = int (input ("Ingrese un segundo nro"))


    opcion = int (input ("Ingrese Ingrese opción: 1. Suma 2. Resta 3.Multiplicación " ))

    while opcion >3 :
        opcion = int (input ("Reingrese una opción válida" ))

    if (opcion ==1):
        print ( nro1+ nro2)
    elif (opcion ==2):
        print ( nro1-nro2)
    else:
        print (nro1*nro2)


if __name__ == '__main__':
    main()
