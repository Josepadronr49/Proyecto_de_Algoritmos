class Mision:
    def __init__(self,nombre_mision, planeta_destino, naves, armas, integrantes):
        self.nombre_mision=nombre_mision
        self.planeta_destino=planeta_destino
        self.naves=naves
        self.armas=armas
        self.integrantes=integrantes

mision_obj=[]
while True:
    opcion=input("""Seleccione la ocpión de su preferencia:
1- Crear misiones
2- Modifica tu mision
3- Visualiza tus misiones
4- Guarda tus misiones
5- Carga tus misiones     
6- Salir      
--->""")
    if opcion=="1":
        if len(mision_obj)<=5:
            nombre_de_la_mision=input("Ingrese el nombre de la misión: ")
            planeta_destino_mision=input("Ingrese el nombre de la misión: ")
            naves_mision=input("Ingrese el nombre de la misión: ")
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
            mision_obj.append(Mision(nombre_de_la_mision,planeta_destino_mision,naves_mision,armas_mision,integrantes_mision))
            print("¡Su misión ha sido creada con éxito!")
        else:
            print("Solo se pueden definir hasta 5 misiones")

    elif opcion=="2":
        None
    elif opcion=="3":
        None
    elif opcion=="4":
        None
    elif opcion=="5":
        None
    elif opcion=="6":
        break
    else:
        print("Ingrese una opción válida")

        