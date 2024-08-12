class Mision:
    def __init__(self, nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision=nombre_mision
        self.planeta_destino=planeta_destino
        self.nave=nave
        self.armas=(armas)
        self.integrantes=(integrantes)

    def mostra_mision(self):
        print(f"El nombre de la misión es: {self.nombre_mision}")
        print(f"El planeta de la misión es: {self.planeta_destino}")
        print(f"La nave de la misión es: {self.nave}")
        print(f"Las armas de la misión es: {self.armas}")
        print(f"Los integrantes de la misión es: {self.integrantes}")