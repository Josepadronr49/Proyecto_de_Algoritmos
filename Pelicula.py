#Se crea la clase de los planetas para luego convertir la información de la Api a objetos 
class Pelicula:
    def __init__(self, titulo, numero_episodio, fecha_lanzamiento, texto_inicio, director):
        self.titulo=titulo
        self.numero_episodio=numero_episodio
        self.fecha_lanzamiento=fecha_lanzamiento
        self.texto_inicio=texto_inicio
        self.director=director

    def mostrar_pelicula(self):
        print(f"a-Título: {self.titulo}")
        print(f"b-Número del episodio: {self.numero_episodio}")
        print(f"c-Fecha de Lanzamiento: {self.fecha_lanzamiento}")
        print(f"d-Texto de Inicio: {self.texto_inicio}")
        print(f"e-Director: {self.director}")
        