#-------------------------------------------------------------------------------
'''
Pedir al usuario que ingrese un email
Verificar si el usuario ingresó una dirección de email (basta con que tenga un
"@")
Al finalizar mostrar por pantalla si es un email o no
No utilizar in
'''
#-------------------------------------------------------------------------------

def main():
    pass

    email = str(input ("Ingrese su mail: "))

    if email.count("@"):
        print ("El elemento ingresado es un email")

    else:
        print("El elemento ingresado no es un email")









if __name__ == '__main__':
    main()
