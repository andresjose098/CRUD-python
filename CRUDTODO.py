# Modelo
class Nota:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

# Repositorio de Notas
class RepositorioNotas:
    def __init__(self):
        self.notas = []
    
    def crear_nota(self, nota):
        self.notas.append(nota)
    
    def obtener_nota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                return nota
        return None
    
    def actualizar_nota(self, titulo, nuevo_titulo, nuevo_contenido):
        nota = self.obtener_nota(titulo)
        if nota:
            nota.titulo = nuevo_titulo
            nota.contenido = nuevo_contenido
            return True
        return False
    
    def eliminar_nota(self, titulo):
        for i, nota in enumerate(self.notas):
            if nota.titulo == titulo:
                del self.notas[i]
                return True
        return False
    
    def listar_notas(self):
        return self.notas

# Controlador
class ControladorNotas:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def ejecutar_operacion(self, operacion, *args):
        operaciones = {
            "crear": self.repositorio.crear_nota,
            "obtener": self.repositorio.obtener_nota,
            "actualizar": self.repositorio.actualizar_nota,
            "eliminar": self.repositorio.eliminar_nota,
            "listar": self.repositorio.listar_notas
        }
        return operaciones[operacion](*args)

# Vista y Entrada del Usuario
def vista_principal(controlador):
    while True:
        operacion = input("Introduce la operación (crear, obtener, actualizar, eliminar, listar, salir): ")
        if operacion == "salir":
            break
        elif operacion == "crear":
            titulo = input("Título de la nota: ")
            contenido = input("Contenido de la nota: ")
            nota = Nota(titulo, contenido)
            controlador.ejecutar_operacion(operacion, nota)
        elif operacion == "obtener":
            titulo = input("Título de la nota: ")
            nota = controlador.ejecutar_operacion(operacion, titulo)
            if nota:
                print(f"Título: {nota.titulo}, Contenido: {nota.contenido}")
            else:
                print("Nota no encontrada")
        elif operacion == "actualizar":
            titulo = input("Título de la nota a actualizar: ")
            nuevo_titulo = input("Nuevo título de la nota: ")
            nuevo_contenido = input("Nuevo contenido de la nota: ")
            if controlador.ejecutar_operacion(operacion, titulo, nuevo_titulo, nuevo_contenido):
                print("Nota actualizada con éxito.")
            else:
                print("No se encontró la nota para actualizar.")
        elif operacion == "eliminar":
            titulo = input("Título de la nota a eliminar: ")
            if controlador.ejecutar_operacion(operacion, titulo):
                print("Nota eliminada con éxito.")
            else:
                print("No se encontró la nota para eliminar.")
        elif operacion == "listar":
            notas = controlador.ejecutar_operacion(operacion)
            for nota in notas:
                print(f"Título: {nota.titulo}, Contenido: {nota.contenido}")

if __name__ == "__main__":
    repositorio = RepositorioNotas()
    controlador = ControladorNotas(repositorio)
    vista_principal(controlador)
