class Planetas: #Transformacion de los datos a la clase planeta
    def __init__(self,nombre,periodo_de_orbita,periodo_de_rotacion,cantidad_de_habitantes,clima,lista_episodio,lista_personajes):
        self.nombre=nombre
        self.periodo_de_orbita=periodo_de_orbita
        self.periodo_de_rotacion=periodo_de_rotacion
        self.cantidad_de_habitantes=cantidad_de_habitantes
        self.clima=clima
        self.lista_episodio=lista_episodio
        self.lista_personajes=lista_personajes 
    def mostrar_planeta(self):
        print(f'nombre es: {self.nombre}')
        print(f'periodo de orbita: {self.periodo_de_orbita}')
        print(f'periodo de rotacion: {self.periodo_de_rotacion}')
        print(f'cantidad de habitantes: {self.cantidad_de_habitantes}')
        print(f'clima: {self.clima}')
        print(f'lista_episodios {self.lista_episodio}')
        print(f'lista de personajes: {self.lista_personajes}')
        print()
        