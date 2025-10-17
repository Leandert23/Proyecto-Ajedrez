import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkcalendar import DateEntry
from tkinter import ttk

#Interfaz1
def interfazTorneo1():
    #Funciones
    def crearTorneo():
        if vl.validarNombre(entryNombre.get()):
            nombre = entryNombre.get()
        else:
            labelError.config(text="!!El nombre solo debe tener \n caracteres alfanúmericos!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        fecha = entryFecha.get_date()

        if vl.validarEntero(entryParticipantes.get()):
            participantes = entryParticipantes.get()
        else:
            labelError.config(text="!!La cantidad de participantes debe ser \n un numero entero mayor a 0 y menor a 1000", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarEntero(entryRondas.get()):
            rondas = entryRondas.get()
        else:
            labelError.config(text="!!La cantidad de rondas debe ser \n un numero entero mayor a 0 y menor a 100", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return    

        if checkValor.get() == 1:
            invitados = "True"
        else:
            invitados = "False"

        if vl.validarTexto(entryDescripcion.get()):
            descripcion = entryDescripcion.get()
        else:
            labelError.config(text="!!La descripción no debe exceder \n los 15 caracteres!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        respuesta = bd.crearTablaAntesTorneo(nombre, fecha, participantes, rondas, invitados, descripcion)
        if respuesta == True:
            labelError.config(text="!!Ya existe un torneo con estos datos \n por favor ingrese uno nuevo!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        labelError.config(text=f"!!Torneo creado con exito \n {respuesta}!!", bg="lightgray", font=12)
        labelError.after(2000, lambda:(ventana.destroy(), interfazTorneo2(respuesta)))

    #Ventana
    ventana = tk.Tk()
    ventana.title("Torneo")
    anchoVentana = 400
    altoVentana = 450
    x = (ventana.winfo_screenwidth() - anchoVentana)//2
    y = (ventana.winfo_screenheight() - altoVentana)//2
    ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventana.resizable(False, False)
    ventana.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventana, text="Crear torneo", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventana, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelNombre = tk.Label(frame, text="Nombre", font= 20)
    labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelFecha = tk.Label(frame, text="Fecha", font= 20)
    labelFecha.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelParticipantes = tk.Label(frame, text="Participantes", font= 20)
    labelParticipantes.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelRondas = tk.Label(frame, text="Rondas", font= 20)
    labelRondas.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelInvitados = tk.Label(frame, text="Invitados", font= 20)
    labelInvitados.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    labelDescripcion = tk.Label(frame, text="Descripción", font= 20)
    labelDescripcion.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    entryNombre = tk.Entry(frame, font=20)
    entryNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    entryNombre.focus()

    entryFecha = DateEntry(frame, date_pattern='dd-mm-yy', bg="gray", font=20, state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entryParticipantes = tk.Entry(frame, font=20)
    entryParticipantes.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entryRondas = tk.Entry(frame, font=20)
    entryRondas.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    checkValor = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValor, onvalue=1, offvalue=0)
    checkInvitados.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame, font=20)
    entryDescripcion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=lambda: [entryNombre.delete(0, tk.END), 
                                                                     entryParticipantes.delete(0, tk.END), 
                                                                     entryFecha.config(state="normal"),
                                                                     entryFecha.delete(0, tk.END), 
                                                                     entryFecha.config(state="readonly"),
                                                                     checkInvitados.deselect(), 
                                                                     entryDescripcion.delete(0, tk.END),
                                                                     entryNombre.focus()])
    botonLimpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    botonCrear = tk.Button(frame, text="Crear", font=20,  command=crearTorneo)
    botonCrear.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
    ventana.mainloop()

def interfazTorneo2(nombre):
    #Funciones
    def cargarJugadores():
        for dato in tabla.get_children():
            tabla.delete(dato)
    #Ventana
    ventana = tk.Tk()
    ventana.title("Torneo")
    anchoVentana = 700
    altoVentana = 450
    x = (ventana.winfo_screenwidth() - anchoVentana)//2
    y = (ventana.winfo_screenheight() - altoVentana)//2
    ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventana.resizable(False, False)
    ventana.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventana, text=f"{nombre}", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventana, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 15, rowheight=30)
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido", "Elo", "Victorias", "Tablas", "Derrotas", "Puntos", "Desempates"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=8, padx=5, pady=10, sticky="ew")

    #tabla.column("Posición", anchor=tk.CENTER, width=70)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=170)
    tabla.column("Elo", anchor=tk.CENTER, width=45)
    tabla.column("Victorias", anchor=tk.CENTER, width=70)
    tabla.column("Tablas", anchor=tk.CENTER, width=55)
    tabla.column("Derrotas", anchor=tk.CENTER, width=70)
    tabla.column("Puntos", anchor=tk.CENTER, width=60)
    tabla.column("Desempates", anchor=tk.CENTER, width=100)

    #if len(nombreCompleto) > 20:
        #nombreCompleto = nombreCompleto[:15] + "..."
    #tabla.heading("Posición", text="Posición")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Elo", text="Elo")
    tabla.heading("Victorias", text="Victorias")
    tabla.heading("Tablas", text="Tablas")
    tabla.heading("Derrotas", text="Derrotas")
    tabla.heading("Puntos", text="Puntos")
    tabla.heading("Desempates", text="Desempates")

    tabla.insert("", tk.END, values=("Juan Perez", 1500, 3, 1, 0, 3.5, "2.5 / 1.5"))

    if len(tabla.get_children()) > 10:
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
        tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=8, sticky="ns")
    

    ventana.mainloop()

def editarTorneo():
    pass

def borrarTorneo():
    pass

def filtrarTorneos():
    pass

if __name__ == "__main__":
    interfazTorneo1()
    #interfazTorneo2("x")

#5to poder
#El nombre de la rosa
#Farenheit 451 1966/2018