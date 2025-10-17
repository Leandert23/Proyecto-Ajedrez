import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkcalendar import DateEntry
from tkinter import ttk


def interfazJugadores1():
    #Funciones
    def cargarJugadores():
        datos = bd.consultarDatosJugadores()
        for registro in datos:
            nombreCompleto = registro[0]
            if len(nombreCompleto) > 20:
                nombreCompleto = nombreCompleto[:15] + "..."
            tabla.insert("", tk.END, values=(nombreCompleto, registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]))
        
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

    botonCrearJugador = tk.Button(ventana, text="Crear Jugador", font=15, command=lambda:(ventana.destroy(), interfazJugadores2()))
    botonCrearJugador.pack()
    

    cargarJugadores()
    ventana.mainloop()


def interfazJugadores2():
    #Funciones
    def crearTorneo():
        if checkValorInvitado.get() == 1:
            invitado = "Si"
        else:
            invitado = "No"

        if vl.validarNombre(entryNombreCompleto.get()):
            nombreCompleto = entryNombreCompleto.get()
        else:
            labelError.config(text="!!El nombre solo debe tener \n caracteres alfanúmericos!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarTexto(entryGenero.get()):
            genero = entryGenero.get()
        else:
            labelError.config(text="!!El Género \n no debe exceder los 15 caracteres!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarTexto(entryFacultad.get()):
            facultad = entryFacultad.get()
        else:
            labelError.config(text="!!El nombre de la Facultad \n no debe exceder los 15 caracteres!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarEntero(entryElo.get()):
            elo = entryElo.get()
        else:
            labelError.config(text="!!El elo debe ser \n un numero entero mayor a 0 y menor a 3000", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
           
        if vl.validarEntero(entryVictorias.get()):
            victorias = entryVictorias.get()
        else:
            labelError.config(text="!!El número de victorias debe ser \n un numero entero positivo menor a 99", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarEntero(entryTorneos.get()):
            torneos = entryTorneos.get()
        else:
            labelError.config(text="!!El número de tornos debe ser \n un numero entero positivo menor a 99", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        respuesta = bd.agregarDatosJugadores(nombreCompleto, genero, facultad, elo, victorias, torneos, invitado)
        if respuesta == True:
            labelError.config(text="!!Ya existe un Jugador con estos datos \n por favor ingrese uno nuevo!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        labelError.config(text=f"!!Jugador creado con exito \n {respuesta}!!", bg="lightgray", font=12)
        labelError.after(2000, lambda:(ventana.destroy(), interfazJugadores1()))

    def invitado():
        entryElo.config(state=tk.NORMAL)
        entryElo.delete(0, tk.END)
        entryVictorias.config(state=tk.NORMAL)
        entryVictorias.delete(0, tk.END)
        entryTorneos.config(state=tk.NORMAL)
        entryTorneos.delete(0, tk.END)
        if checkValorInvitado.get() == 1:
            checkValorNuevo.set(0)
            entryFacultad.insert(0, "Invitado")
            entryFacultad.config(state=tk.DISABLED)
            entryElo.insert(0, "1600")
            entryElo.config(state=tk.DISABLED)
            return
        entryFacultad.config(state=tk.NORMAL)
        entryFacultad.delete(0, tk.END)
        entryElo.config(state=tk.NORMAL)  
        entryElo.delete(0, tk.END)
    
    def nuevoJugador():
        entryFacultad.config(state=tk.NORMAL)
        entryFacultad.delete(0, tk.END)
        entryElo.config(state=tk.NORMAL)  
        entryElo.delete(0, tk.END)
        if checkValorNuevo.get() == 1:
            checkValorInvitado.set(0)
            entryElo.insert(0, "1500")
            entryElo.config(state=tk.DISABLED)
            entryVictorias.insert(0, "0")
            entryVictorias.config(state=tk.DISABLED)
            entryTorneos.insert(0, "0")
            entryTorneos.config(state=tk.DISABLED)
            return
        entryElo.config(state=tk.NORMAL)
        entryElo.delete(0, tk.END)
        entryVictorias.config(state=tk.NORMAL)
        entryVictorias.delete(0, tk.END)
        entryTorneos.config(state=tk.NORMAL)
        entryTorneos.delete(0, tk.END)

    #Ventana
    ventana = tk.Tk()
    ventana.title("Jugadores")
    anchoVentana = 400
    altoVentana = 500
    x = (ventana.winfo_screenwidth() - anchoVentana)//2
    y = (ventana.winfo_screenheight() - altoVentana)//2
    ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventana.resizable(False, False)
    ventana.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventana, text="Agregar Jugador", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventana, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    checkValorNuevo = tk.IntVar()
    checkJugadorNuevo= tk.Checkbutton(frame, text="Jugador Nuevo", variable=checkValorNuevo, onvalue=1, offvalue=0, command=nuevoJugador)
    checkJugadorNuevo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    checkValorInvitado = tk.IntVar()
    checkJugadorInvitado= tk.Checkbutton(frame, text="Invitado", variable=checkValorInvitado, onvalue=1, offvalue=0, command=invitado)
    checkJugadorInvitado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    labelNombreCompleto = tk.Label(frame, text="Nombre y Apellido", font= 20)
    labelNombreCompleto.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelGenero = tk.Label(frame, text="Género", font= 20)
    labelGenero.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelFacultad = tk.Label(frame, text="Facultad", font= 20)
    labelFacultad.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelElo = tk.Label(frame, text="Elo", font= 20)
    labelElo.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    labelVictorias = tk.Label(frame, text="Victorias", font= 20)
    labelVictorias.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    labelTorneos = tk.Label(frame, text="Torneos", font= 20)
    labelTorneos.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    entryNombreCompleto = tk.Entry(frame, font=20)
    entryNombreCompleto.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    entryNombreCompleto.focus()

    entryGenero = tk.Entry(frame, font=20)
    entryGenero.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entryFacultad = tk.Entry(frame, font=20)
    entryFacultad.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entryElo = tk.Entry(frame, font=20)
    entryElo.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryVictorias = tk.Entry(frame, font=20)
    entryVictorias.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    entryTorneos = tk.Entry(frame, font=20)
    entryTorneos.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=lambda: [checkValorInvitado.set(0), checkValorNuevo.set(0),
                                                                    entryNombreCompleto.delete(0, tk.END), entryGenero.delete(0, tk.END),
                                                                    entryFacultad.config(state=tk.NORMAL), entryFacultad.delete(0, tk.END), 
                                                                    entryElo.config(state=tk.NORMAL), entryElo.delete(0, tk.END), 
                                                                    entryVictorias.config(state=tk.NORMAL), entryVictorias.delete(0, tk.END), 
                                                                    entryTorneos.config(state=tk.NORMAL), entryTorneos.delete(0, tk.END), 
                                                                    entryNombreCompleto.focus()])
    botonLimpiar.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

    botonAgregar = tk.Button(frame, text="Agregar", font=20,  command=crearTorneo)
    botonAgregar.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

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
    interfazJugadores1()
