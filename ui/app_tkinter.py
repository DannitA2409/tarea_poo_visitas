import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class AppVisitas:
    # INYECCIÓN DE DEPENDENCIAS: Recibe el servicio ya instanciado desde afuera
    def __init__(self, root, servicio):
        self.root = root
        self.root.title("Gestión de Visitantes")
        self.root.geometry("650x500")
        self.servicio = servicio

        self._crear_formulario()
        self._crear_botones()
        self._crear_tabla()

    def _crear_formulario(self):
        """Crea el panel superior con los campos de entrada."""
        frame_form = tk.LabelFrame(self.root, text="Datos del Visitante", padx=10, pady=10)
        frame_form.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_form, text="Cédula:").grid(row=0, column=0, pady=5, sticky="e")
        self.entry_cedula = tk.Entry(frame_form, width=30)
        self.entry_cedula.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Nombre Completo:").grid(row=1, column=0, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Motivo de Visita:").grid(row=2, column=0, pady=5, sticky="e")
        self.entry_motivo = tk.Entry(frame_form, width=30)
        self.entry_motivo.grid(row=2, column=1, padx=5, pady=5)

    def _crear_botones(self):
        """Crea el panel central con los botones de acción."""
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=5)

        tk.Button(frame_btn, text="Registrar", bg="#4CAF50", fg="white", command=self.evento_registrar).grid(row=0, column=0, padx=10)
        tk.Button(frame_btn, text="Eliminar Selección", bg="#f44336", fg="white", command=self.evento_eliminar).grid(row=0, column=1, padx=10)
        tk.Button(frame_btn, text="Limpiar Campos", bg="#2196F3", fg="white", command=self.evento_limpiar).grid(row=0, column=2, padx=10)

    def _crear_tabla(self):
        """Crea la tabla dinámica para visualizar los registros."""
        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(padx=10, pady=10, fill="both", expand=True)

        columnas = ("cedula", "nombre", "motivo")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre Completo")
        self.tabla.heading("motivo", text="Motivo")

        self.tabla.column("cedula", width=100, anchor="center")
        self.tabla.column("nombre", width=200, anchor="w")
        self.tabla.column("motivo", width=250, anchor="w")

        self.tabla.pack(fill="both", expand=True)

    # EVENTOS
    def evento_registrar(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        # Validación visual de campos vacíos
        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Instancia el modelo y lo envia al servicio
        visitante = Visitante(cedula, nombre, motivo)
        exito, mensaje = self.servicio.registrar_visitante(visitante)

        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.actualizar_tabla()
            self.evento_limpiar()
        else:
            messagebox.showerror("Error", mensaje)

    def evento_eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Seleccione un visitante de la tabla para eliminar.")
            return

        # Extrae la cédula de la fila seleccionada
        item = self.tabla.item(seleccion[0])
        cedula_seleccionada = str(item['values'][0])

        exito, mensaje = self.servicio.eliminar_visitante(cedula_seleccionada)
        if exito:
            messagebox.showinfo("Eliminado", mensaje)
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)

    def evento_limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)
        self.entry_cedula.focus()

    def actualizar_tabla(self):
        """Refresca la vista de la tabla consultando los datos del servicio."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        visitantes = self.servicio.obtener_visitantes()
        for v in visitantes:
            self.tabla.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))