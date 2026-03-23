class Visitante:
    """Representa la entidad Visitante en el sistema."""
    
    def __init__(self, cedula: str, nombre: str, motivo: str):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__motivo = motivo

    # Getters para acceder a los datos privados
    @property
    def cedula(self):
        return self.__cedula

    @property
    def nombre(self):
        return self.__nombre

    @property
    def motivo(self):
        return self.__motivo