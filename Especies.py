class Especies: #Transformacion de los datos a la clase de especie
    def __init__(self,nombre,altura,clasificacion,planeta,lengua_materna,nombre_de_los_personajes_de_especie,nombre_de_episodios):
        self.nombre=nombre
        self.altura=altura
        self.clasificacion=clasificacion
        self.planeta=planeta
        self.lengua_materna=lengua_materna
        self.nombre_de_los_personajes_de_especie=nombre_de_los_personajes_de_especie
        self.nombre_de_episodios=nombre_de_episodios
        
    def mostrar_especies(self):
        print(f'a-Nombre: {self.nombre}')
        print(f'b-Altura: {self.altura}')
        print(f'c-Clasificacion: {self.clasificacion}')
        print(f'd-Planeta: {self.planeta}')
        print(f'e-Lengua materna: {self.lengua_materna}')
        print(f'f-Nombre de los personajes: {self.nombre_de_los_personajes_de_especie}')
        print(f'g-Nombre de los episodios: {self.nombre_de_episodios}')
        print()
        
        
        