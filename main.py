import tkinter as tk
import torneo, datos, jugadores, baseDatos
import sys
ventanaMain = tk.Tk()
ventanaMain.title("Ajedrez")
anchoVentana = 500
altoVentana = 300
x = (ventanaMain.winfo_screenwidth() - anchoVentana)//2
y = (ventanaMain.winfo_screenheight() - altoVentana)//2
ventanaMain.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
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

botonTorneo = tk.Button(ventanaMain, text= "Nuevo Torneo", bg="gray", fg="black", command= interfazTorneo, font=30)
botonTorneo.pack(padx=50, pady= 10, fill=tk.BOTH, expand=True)
botonJugadores = tk.Button(ventanaMain, text= "Jugadores", bg="gray", fg="black", command= interfazJugadores, font=30)
botonJugadores.pack(padx=50, pady=10, fill=tk.BOTH, expand=True)
botonDatos = tk.Button(ventanaMain, text= "Datos", bg="gray", fg="black", command= interfazDatos, font=30)
botonDatos.pack(padx=50, pady=10, fill=tk.BOTH, expand=True)
etiquetaVersion = tk.Label(ventanaMain, text="Versión 1.0", bg="lightgray", fg="black").pack()

baseDatos.crearTablaJugadores()
baseDatos.crearTablaListaTorneos()
baseDatos.crearTablaMedallas()
ventanaMain.mainloop()



