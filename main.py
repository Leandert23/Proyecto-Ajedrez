import tkinter as tk
import torneo, datos, jugadores, baseDatos
import sys
ventanaMain = tk.Tk()
ventanaMain.title("ChessPyter")
ventanaMain.geometry(f"{ventanaMain.winfo_screenwidth()}x{ventanaMain.winfo_screenheight()-50}+{-8}+{-2}")
ventanaMain.configure(bg="lightgray")
ventanaMain.protocol("WM_DELETE_WINDOW", lambda: (ventanaMain.destroy(), sys.exit(0)))

def interfazTorneo():
    ventanaMain.withdraw()
    torneo.interfazTorneo1(ventanaMain)

def interfazJugadores():
    ventanaMain.withdraw()
    jugadores.interfazJugadores1(ventanaMain)

def interfazDatos():
    ventanaMain.withdraw()
    datos.interfazDatos1(ventanaMain)

labelTitulo = tk.Label(ventanaMain, text=f"  ChessPyter  ", font=("Impact", 25))
labelTitulo.pack(pady=(30,15))

frame = tk.Frame(ventanaMain, bd=10, bg="gray", width=500, height=400)
frame.pack()
frame.pack_propagate(False) 

botonTorneo = tk.Button(frame, text= "Nuevo Torneo", bg="lightgray", command= interfazTorneo, font=("Impact", 20))
botonTorneo.pack(padx=20, pady= (20,10),fill=tk.BOTH, expand=True)
botonJugadores = tk.Button(frame, text= "Jugadores", bg="lightgray", command= interfazJugadores, font=("Impact", 20))
botonJugadores.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
botonDatos = tk.Button(frame, text= "Datos", bg="lightgray", command= interfazDatos, font=("Impact", 20))
botonDatos.pack(padx=20, pady=(10,20), fill=tk.BOTH, expand=True)
etiquetaVersion = tk.Label(ventanaMain, text="Versión 2.0", bg="lightgray", font=("Impact", 12))
etiquetaVersion.pack(side="bottom", pady=30)

baseDatos.crearTablaJugadores()
baseDatos.crearTablaListaTorneos()
baseDatos.crearTablaMedallas()
ventanaMain.mainloop()