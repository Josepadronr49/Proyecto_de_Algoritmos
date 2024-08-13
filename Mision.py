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
    def agregar_arma(self,arma,lista_objeto,lista_armas): 
        for elemento in lista_objeto:
            if len(elemento.armas) < 7:
                for elemento_arma in lista_armas:
                        if arma.isnumeric() and int(arma) < 60:
                            elemento.armas.append(elemento_arma[int(arma)])
            else:
                print("No se pueden agregar más de 7 armas")
    
     #Se crea una función para eliminar armas
    def eliminar_arma(self,arma,lista_objeto):
        for elemento in lista_objeto:
            arma_lista=list(elemento.armas)
            if arma<len(arma_lista):
                del arma_lista[arma]
                elemento.armas=arma_lista
            else:
                print("El arma que quiere eliminar no está en la lista")

    #Se crea una función para agregar integrantes manteniendo el límite de hasta 7 integrantes
    def agregar_integrante(self,integrante,lista_objeto,lista_elementos):
        for elemento in lista_objeto:
            if len(elemento.integrantes) < 7:
                for elemento_integrante in lista_elementos:
                        if integrante.isnumeric() and int(integrante) < 96:
                            elemento.armas.append(elemento_integrante[int(integrante)])
            else:
                print("No se pueden agregar más de 7 integrantes")
    
    #Se crea una función para eliminar integrantes
    def eliminar_integrante(self, integrante,lista_objeto):
        for elemento in lista_objeto:
            integrante_lista=list(elemento.integrantes)
            if integrante< len(integrante_lista):
                del integrante_lista[integrante]
                elemento.integrantes=integrante_lista
            else:
                print("El integrante que quiere eliminar no está en la lista")