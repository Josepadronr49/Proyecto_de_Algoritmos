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
        print(f'a-Nombre es: {self.nombre}')
        print(f'b-Periodo de orbita: {self.periodo_de_orbita}')
        print(f'c-Periodo de rotacion: {self.periodo_de_rotacion}')
        print(f'd-Cantidad de habitantes: {self.cantidad_de_habitantes}')
        print(f'e-Clima: {self.clima}')
        print(f'f-Lista_episodios {self.lista_episodio}')
        print(f'g-Lista de personajes: {self.lista_personajes}')
        print()
        