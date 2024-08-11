class Mision:
    def __init__(self,nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision=nombre_mision
        self.planeta_destino=planeta_destino
        self.nave=nave
        self.armas=armas
        self.integrantes=integrantes


def lista_misiones():
    if mision_obj:
        for i, mision in enumerate(mision_obj):
            print(f"{i}:{mision.nombre_mision}")
    else:
        print("No hay misiones definidas aún")

mision_obj=[]
while True:
    eleccion=input("""Seleccione la ocpión de su preferencia:
1- Crear misiones
2- Modifica tu mision
3- Visualiza tus misiones
4- Guarda tus misiones
5- Carga tus misiones     
6- Salir      
--->""")
    if eleccion=="1":
        if len(mision_obj)<=5:
            nombre_de_la_mision=input("Ingrese el nombre de la misión: ")
            planeta_destino_mision=input("Ingrese el planeta destino de la misión: ")
            nave_mision=input("Ingrese la nave de la misión: ")
            armas_mision=[]
            integrantes_mision=[]
            while len(armas_mision)<=7:
                arma=input("Ingrese el arma que desee utilizar: ")
                if arma:
                    armas_mision.append(arma)
                else:
                    break
            while len(integrantes_mision)<=7:
                integrante=input("Ingrese los integrantes de su misión: ")
                if integrante:
                    integrantes_mision.append(integrante)
                else:
                    break
            mision_obj.append(Mision(nombre_de_la_mision,planeta_destino_mision,nave_mision,armas_mision,integrantes_mision))
            print("¡Su misión ha sido creada con éxito!")
        else:
            print("Solo se pueden definir hasta 5 misiones")

    elif eleccion=="2":
        lista_misiones()
        seleccion=int(input("""
Seleccion el número de la misión que desee modificar 
--->"""))
        if 0 <= seleccion < len(mision_obj):
            mision_modificar=mision_obj[seleccion]
            print(f"Modificando mision: {mision_modificar.nombre_mision}")

            while True:
                elegir=input("""
Seleccione la característica de la misión que desee modificar:
1- Modificar nombre de la misión
2- Modificar planeta destino de la misión
3- Modificar la nave de la misión
4- Agregar arma
5- Eliminar arma
6- Agregar integrante
7- Eliminar arma
8- Salir                           
--->""") 
                if elegir =="1":
                    mision_modificar.nombre_mision=input("Ingrese el nombre modificado de la misión: ")

                elif elegir =="2":
                    mision_modificar.planeta_destino=input("Ingrese el planeta modificado: ")

                elif elegir =="3":
                    mision_modificar.nave=input("Ingrese la nave modificada: ")

                elif elegir =="4":
                    nueva_arma=input("Ingrese la nueva arma que desea agregar: ")
                    mision_modificar.agregar_arma(nueva_arma)

                elif elegir =="5":
                    arma_eliminada=input("Ingrese el arma que desea eliminar: ")
                    mision_modificar.eliminar_arma(arma_eliminada)

                elif elegir =="6":
                    nuevo_integrante=input("Ingrese el nombre del integrante que desea eliminar: ")
                    mision_modificar.agregar_integrante(nuevo_integrante)

                elif elegir =="7":
                    integrante_eliminado=input("Ingrese el nombre del integrante que desea eliminar: ")
                    mision_modificar.eliminar_arma(integrante_eliminado)

                elif elegir =="8":
                    break

                else:
                    print("Ingrese una opción válida")
        
        else:
            print("Ingrese una opción válida")

    elif eleccion=="3":
        None
    elif eleccion=="4":
        None
    elif eleccion=="5":
        None
    elif eleccion=="6":
        break
    else:
        print("Ingrese una opción válida")

def agregar_arma(arma):
    if len(armas_mision) < 7:
        armas_mision.append(arma)
    else:
        print("No se pueden agregar más de 7 armas")

def elemininar_arma(arma):
    if arma in armas_mision:
        armas_mision.remove(arma)
    else:
        print("El arma que quiere eliminar no está en la lista")

def agregar_integrante(integrante):
    if len(integrantes_mision) < 7:
        integrantes_mision.append(integrante)
    else:
        print("No se pueden agregar más de 7 integrantes")

def eliminar_integrante(integrante):
    if integrante in integrantes_mision:
        integrantes_mision.remove(integrante)
    else:
        print("El integrante que quiere eliminar no está en la lista")

        