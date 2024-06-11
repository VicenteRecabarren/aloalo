import os
agenda={}
opcionInicial=0
nombre=""
celular=0

def limpiar_pantalla():
    os.system('cls')

def pausar_pantalla():
    os.system('pause')

def mensajes_contextuales():
    if opcionInicial==1:
        print("Añadir/Modificar")
    elif opcionInicial==2:
        print("Buscar")
    elif opcionInicial==3:
        print("Borrar")
    elif opcionInicial==4:
        print("Listar")
    elif opcionInicial==5:
        print("Salir")
    else:
        print("Dato no válido")
        
def iterar_diccionario():
    for i in agenda:
        print(i)
        
def menu_principal():
    print("Bienvenidos\n1)Añadir/Modificar\n2)Buscar\n3)Borrar\n4)Listar\n5)Salir ")
    opcionInicial=int(input("Ingrese su opción: "))
    return opcionInicial

def conseguir_nombres():
    nombre=str(input("Ingrese un nombre: "))
    return nombre

def conseguir_celulares():
    celular=int(input("Ingrese número de celular: "))
    return celular

while True:
    #Falta Try individual y while individual
    limpiar_pantalla()
    opcionInicial=menu_principal()
    if opcionInicial==1:
        #AÑADIR Y MODIFICAR
        limpiar_pantalla()
        mensajes_contextuales()
        nombre=conseguir_nombres()
        celular=conseguir_celulares()
        """
        if nombre==agenda[nombre]:
            print(f"El nombre: {nombre} ya se encuentra registrado el número de teléfono es: {agenda[nombre]}")
        """
        agenda[nombre] = celular
        #Falta que permita Modificar el nombre, que nombre solo sea una cadena, que pueda mostrar que un nombre ya existe junto con su telefono...
        pausar_pantalla()
    elif opcionInicial==2:
        #BUSCAR
        limpiar_pantalla()
        mensajes_contextuales()
        #Falta Desarrollo
        pausar_pantalla()
    elif opcionInicial==3:
        #BORRAR
        limpiar_pantalla()
        mensajes_contextuales()
        #Falta Desarrollo
        pausar_pantalla()
    elif opcionInicial==4:
        #LISTAR
        limpiar_pantalla()
        mensajes_contextuales()
        #Falta Mostrar números
        iterar_diccionario()
        pausar_pantalla()
    elif opcionInicial==5:
        #SALIR
        limpiar_pantalla()
        mensajes_contextuales()
        pausar_pantalla()
        break
        #Faltan "detalles"
    else:
        limpiar_pantalla()
        mensajes_contextuales()
        pausar_pantalla()
        #Terminado
print("DEPURACIÓN")
print(agenda)