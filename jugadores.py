import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkinter import ttk

def interfazTorneo1():
    #Funciones
    def cargarJugadores():
        datos = bd.consultarDatosJugadores()
        for registro in datos:
            nombreCompleto = f"{registro[0]} {registro[1]}"
            if len(nombreCompleto) > 20:
                nombreCompleto = nombreCompleto[:15] + "..."
            tabla.insert("", tk.END, values=(nombreCompleto, registro[2], registro[3], registro[4], registro[5], registro[6], registro[7]))
        
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
            
            
    #Ventana
    ventana = tk.Tk()
    ventana.title("Jugadores")
    anchoVentana = 700
    altoVentana = 350
    x = (ventana.winfo_screenwidth() - anchoVentana)//2
    y = (ventana.winfo_screenheight() - altoVentana)//2
    ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventana.resizable(False, False)
    ventana.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventana, text=f"Jugadores", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventana, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido", "Género", "Facultad", "Elo", "Victorias", "Torneos", "Invitado"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Género", anchor=tk.CENTER, width=70)
    tabla.column("Facultad", anchor=tk.CENTER, width=80)
    tabla.column("Elo", anchor=tk.CENTER, width=50)
    tabla.column("Victorias", anchor=tk.CENTER, width=70)
    tabla.column("Torneos", anchor=tk.CENTER, width=70)
    tabla.column("Invitado", anchor=tk.CENTER, width=70)

    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Género", text="Género")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Elo", text="Elo")
    tabla.heading("Victorias", text="Victorias")
    tabla.heading("Torneos", text="Torneos")
    tabla.heading("Invitado", text="Invitado")
    
    


    cargarJugadores()
    ventana.mainloop()

def añadirJugador():
    pass

def editarJugador():
    pass

def borrarJugador():
    pass

def filtarJugador():
    pass

def  listaJugadores():
    pass

if __name__ == "__main__":
    interfazTorneo1()
