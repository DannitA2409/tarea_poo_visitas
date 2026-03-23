from modelos.visitante import Visitante

class VisitaServicio:
    """Clase encargada de la lógica de negocio (CRUD) de los visitantes."""
    
    def __init__(self):
        # Colección interna encapsulada.
        self.__visitantes = {}

    def registrar_visitante(self, visitante: Visitante):
        """Registra un visitante validando que la cédula no esté duplicada."""
        if visitante.cedula in self.__visitantes:
            return False, f"El visitante con cédula {visitante.cedula} ya está registrado."
        
        self.__visitantes[visitante.cedula] = visitante
        return True, "Visitante registrado exitosamente."

    def obtener_visitantes(self):
        """Retorna una lista con todos los objetos Visitante."""
        return list(self.__visitantes.values())

    def eliminar_visitante(self, cedula: str):
        """Elimina un visitante del registro por su cédula."""
        if cedula in self.__visitantes:
            del self.__visitantes[cedula]
            return True, "Registro eliminado correctamente."
        return False, "El visitante no existe."