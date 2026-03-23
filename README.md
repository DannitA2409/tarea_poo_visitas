# Sistema de Gestión de Visitantes (CRUD Modular)
Esta es una aplicación de escritorio desarrollada en Python utilizando la librería estándar `tkinter`. Su principal característica es el uso de una arquitectura de software limpia y modular (separación por capas).

## Características principales
- **Modelos:** Contiene la definición de datos (Entidad Visitante).
- **Servicios:** Centraliza la lógica de negocio y las validaciones.
- **UI:** Interfaz gráfica totalmente separada de la lógica.
- **Inyección de Dependencias:** El servicio se acopla a la UI desde el punto de arranque.
- **Operaciones CRUD:** Permite Registrar, Listar y Eliminar visitantes en memoria.

## Requisitos
- Python 3.8 o superior.
- No requiere librerías externas (solo módulos nativos de Python).

## Cómo ejecutar el programa
1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta principal del proyecto (`tarea_poo_visitas/`).
3. Ejecuta el siguiente comando:

```bash
python main.py