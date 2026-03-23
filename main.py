import tkinter as tk
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas

def main():
    # Crea la instancia de Tkinter
    root = tk.Tk()
    
    # Crea la instancia del Servicio (Lógica)
    servicio = VisitaServicio()
    
    # Inyecta la dependencia (servicio) a la capa UI
    app = AppVisitas(root, servicio)
    
    # Inicia el loop de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()