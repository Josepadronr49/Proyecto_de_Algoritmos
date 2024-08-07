#Se crea la clase de los personajes para luego convertir la información de la Api a objetos 
class Personaje: 
    def __init__(self,nombre, planeta, titulo_episodio, genero, especie, naves, vehiculos):
        self.nombre=nombre
        self.planeta=planeta
        self.titulo_episodio=titulo_episodio
        self.genero=genero
        self.especie=especie
        self.naves=naves
        self.vehiculos=vehiculos

    def mostrar_personaje(self):
        print(f"Nombre del Personaje: {self.nombre}")
        print(f"Número del episodio: {self.planeta}")
        print(f"Título de episodio en el que aparece: {self.titulo_episodio}")
        print(f"Género: {self.genero}")
        print(f"Especie: {self.especie}")  
        print(f"Naves: {self.naves}") 
        print(f"Vehículos: {self.vehiculos}") 
