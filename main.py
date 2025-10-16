import tkinter as tk
import torneo, datos, jugadores


ventana = tk.Tk()
ventana.title("Ajedrez")
anchoVentana = 500
altoVentana = 300
x = (ventana.winfo_screenwidth() - anchoVentana)//2
y = (ventana.winfo_screenheight() - altoVentana)//2
ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
ventana.configure(bg="lightgray")
def interfazTorneo():
    ventana.destroy()
    torneo.interfazTorneo1()

def interfazJugadores():
    ventana.destroy()
    jugadores.interfazJugadores()

def interfazDatos():
    ventana.destroy()
    datos.interfazDatos()    


botonTorneo = tk.Button(ventana, text= "Nuevo Torneo", bg="gray", fg="black", command= interfazTorneo, font=30
                        ).pack(padx = 50, pady= 10, fill=tk.BOTH, expand=True)
botonJugadores = tk.Button(ventana, text= "Jugadores", bg="gray", fg="black", command= interfazJugadores, font=30
                           ).pack(padx=50, pady= 10, fill=tk.BOTH, expand=True)
botonDatos = tk.Button(ventana, text= "Datos", bg="gray", fg="black", command= interfazDatos, font=30
                       ).pack(padx=50, pady=10, fill=tk.BOTH, expand=True)
etiquetaVersion = tk.Label(ventana, text="Versión 1.0", bg="lightgray", fg="black").pack()
ventana.mainloop()

