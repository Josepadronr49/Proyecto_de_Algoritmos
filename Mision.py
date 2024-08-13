class Mision:
    def __init__(self, nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision=nombre_mision
        self.planeta_destino=planeta_destino
        self.nave=nave
        self.armas=(armas)
        self.integrantes=(integrantes)

    def mostrar_mision(self):
        print(f"El nombre de la misión es: {self.nombre_mision}")
        print(f"El planeta de la misión es: {self.planeta_destino}")
        print(f"La nave de la misión es: {self.nave}")
        print(f"Las armas de la misión es: {self.armas}")
        print(f"Los integrantes de la misión es: {self.integrantes}")

    #Se crea una función para agregar armas manteniendo el límite de hasta 7 armas
    def agregar_arma(self,arma,lista_arma): 
        if len(self.armas) < 7:
            for elemento_arma in lista_arma:
                if int(arma) < 60:
                    self.armas.append(elemento_arma[int(arma)])
                else:
                    print("Ingrese un índice válido")
        else:
            print("No se pueden agregar más de 7 armas")
    
     #Se crea una función para eliminar armas
    def eliminar_arma(self,arma):
            if arma<len(self.armas):
                del self.armas[arma]
            else:
                print("El arma que quiere eliminar no está en la lista")

    #Se crea una función para agregar integrantes manteniendo el límite de hasta 7 integrantes
    def agregar_integrante(self,integrante,lista_integrante):
        if len(self.integrantes) < 7:
            for elemento_integrante in lista_integrante:
                if int(integrante) < 96:
                    self.integrantes.append(elemento_integrante[int(integrante)])
                else:
                    print("Ingrese un índice válido")
        else:
            print("No se pueden agregar más de 7 integrantes")
    
    #Se crea una función para eliminar integrantes
    def eliminar_integrante(self,integrante):
        if 0<=integrante < len(self.integrantes):
            del self.integrantes[integrante]
        else:
            print("El integrante que quiere eliminar no está en la lista")