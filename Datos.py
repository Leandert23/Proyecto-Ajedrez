import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkinter import ttk
import sys

def interfazDatos1(ventanaMain):
    #Funciones
    def cargarJugadores():
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosRanking()

        if len(datos) > 0:
            labelJugadores.config(text=f"Jugadores: {len(datos)}")
        else:
            labelJugadores.config(text=f"Jugadores: 0")
            return
        
        tag = ""
        posicion = 1
        for registro in datos:
            if registro[2] == "Ingeniería":
                tag = "Ingeniería"
            elif registro[2] == "Sociales":
                tag = "Sociales"
            elif registro[2] == "Arquitectura":
                tag = "Arquitectura"
            elif registro[2] == "Derecho":
                tag = "Derecho"
            elif registro[2] == "Odontología":
                tag = "Odontología"
            elif registro[2] == "Invitado":
                tag = "Invitado"
            else:
                tag = "UJAP"
            tabla.tag_configure("Ingeniería", background="#00008B", foreground="#FFFFFF")
            tabla.tag_configure("Sociales", background="#A52A2A", foreground="#FFFFFF")
            tabla.tag_configure("Arquitectura", background="#402169", foreground="#FFFFFF")
            tabla.tag_configure("Derecho", background="#000000", foreground="#FFFFFF")
            tabla.tag_configure("Odontología", background="#888888", foreground="#FFFFFF")
            tabla.tag_configure("Invitado", background="#73bf00", foreground="#FFFFFF")
            tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")
            
            tabla.insert("", tk.END, values=(posicion, registro[0], registro[2], registro[3], registro[4]), tags=(tag))
            posicion += 1
            
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    """   def actualizarLista():
        print("Actualizando lista de jugadores...")
        for dato in tabla.get_children():
            tabla.delete(dato)
        cargarJugadores()"""

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    #Ventana
    ventanaDatos1 = tk.Toplevel(ventanaMain)
    ventanaDatos1.title("Datos")
    anchoVentana = 550
    altoVentana = 375
    x = (ventanaDatos1.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos1.winfo_screenheight() - altoVentana)//2
    ventanaDatos1.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos1.focus_force()
    ventanaDatos1.grab_set()
    ventanaDatos1.resizable(False, False)
    ventanaDatos1.configure(bg="lightgray")
    ventanaDatos1.bind("<Double-Button-1>", lambda e:desseleccionarFila())
    ventanaDatos1.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos1.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos1, text=f"Ranking", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos1, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("#","Nombre y Apellido", "Facultad", "Elo", "Victorias"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

    tabla.column("#", anchor=tk.CENTER, width=30)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Facultad", anchor=tk.CENTER, width=95)
    tabla.column("Elo", anchor=tk.CENTER, width=50)
    tabla.column("Victorias", anchor=tk.CENTER, width=70)

    tabla.heading("#", text="#")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Elo", text="Elo")
    tabla.heading("Victorias", text="Victorias")

    labelJugadores = tk.Label(ventanaDatos1, text="Jugadores: 0", bg="lightgray", fg="black", font=15)
    labelJugadores.pack(padx=10, pady=10, side=tk.LEFT)

    cargarJugadores()

def interfazDatos2(ventanaMain):
    #Funciones
    def cargarJugadores():
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosListaTorneos()

        if len(datos) > 0:
            labelTorneos.config(text=f"Torneos: {len(datos)}")
        else:
            labelTorneos.config(text=f"Torneos: 0")
            return

        for registro in datos:
            """   if registro[2] == "Ingeniería":
                tag = "Ingeniería"
            elif registro[2] == "Sociales":
                tag = "Sociales"
            elif registro[2] == "Arquitectura":
                tag = "Arquitectura"
            elif registro[2] == "Derecho":
                tag = "Derecho"
            elif registro[2] == "Odontología":
                tag = "Odontología"
            elif registro[2] == "Invitado":
                tag = "Invitado"
            else:
                tag = "UJAP"
            tabla.tag_configure("Ingeniería", background="#00008B", foreground="#FFFFFF")
            tabla.tag_configure("Sociales", background="#A52A2A", foreground="#FFFFFF")
            tabla.tag_configure("Arquitectura", background="#402169", foreground="#FFFFFF")
            tabla.tag_configure("Derecho", background="#000000", foreground="#FFFFFF")
            tabla.tag_configure("Odontología", background="#888888", foreground="#FFFFFF")
            tabla.tag_configure("Invitado", background="#73bf00", foreground="#FFFFFF")
            tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")"""
                                               #nombre, fecha, participantes, rondas, invitados, descripcion
            tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
            
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    """   def actualizarLista():
        print("Actualizando lista de jugadores...")
        for dato in tabla.get_children():
            tabla.delete(dato)
        cargarJugadores()"""

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    #Ventana
    ventanaDatos2 = tk.Toplevel(ventanaMain)
    ventanaDatos2.title("Datos")
    anchoVentana = 700
    altoVentana = 350
    x = (ventanaDatos2.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos2.winfo_screenheight() - altoVentana)//2
    ventanaDatos2.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos2.focus_force()
    ventanaDatos2.grab_set()
    ventanaDatos2.resizable(False, False)
    ventanaDatos2.configure(bg="lightgray")
    ventanaDatos2.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaDatos2.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos2.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos2, text=f"Torneos", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos2, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("Nombre", "Fecha", "Participantes", "Rondas", "Invitados", "Descripción"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

    tabla.column("Nombre", anchor=tk.CENTER, width=150)
    tabla.column("Fecha", anchor=tk.CENTER, width=100)
    tabla.column("Participantes", anchor=tk.CENTER, width=100)
    tabla.column("Rondas", anchor=tk.CENTER, width=65)
    tabla.column("Invitados", anchor=tk.CENTER, width=75)
    tabla.column("Descripción", anchor=tk.CENTER, width=150)

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Participantes", text="Participantes")
    tabla.heading("Rondas", text="Rondas")
    tabla.heading("Invitados", text="Invitados")
    tabla.heading("Descripción", text="Descripción")

    labelTorneos = tk.Label(ventanaDatos2, text="Torneos: 0", bg="lightgray", fg="black", font=15)
    labelTorneos.pack(padx=10, pady=10, side=tk.LEFT)

    cargarJugadores()

def rankingGeneral():
    pass

def rankingFemenino():
    pass

def filtarRanking():
    pass

def listaTorneos():
    pass

def Medallas():
    pass
