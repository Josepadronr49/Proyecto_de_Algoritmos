class Mision:
    def __init__(self, nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision=nombre_mision
        self.planeta_destino=planeta_destino
        self.nave=nave
        self.armas=list(armas)
        self.integrantes=list(integrantes)

    #Se crea una función para agregar armas manteniendo el límite de hasta 7 armas
    def agregar_arma(self,arma): 
        if len(self.armas) < 7:
            self.armas.append(arma)
        else:
            print("No se pueden agregar más de 7 armas")
    
    def eliminar_arma(self,arma):
        if arma in self.armas:
            self.remove(arma)
        else:
            print("El arma que quiere eliminar no está en la lista")

    #Se crea una función para agregar integrantes manteniendo el límite de hasta 7 integrantes
    def agregar_integrante(self,integrante):
        if len(self.integrantes) < 7:
            self.integrantes.append(integrante)
        else:
            print("No se pueden agregar más de 7 integrantes")
    
    def eliminar_integrante(self, integrante):
        if integrante in self.mision_obj.integrantes:
            self.integrantes.remove(integrante)
        else:
            print("El integrante que quiere eliminar no está en la lista")