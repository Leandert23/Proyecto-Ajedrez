import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkcalendar import Calendar, DateEntry

#Funciones
def interfazTorneo():
    def crearTorneo():
        if vl.validarNombre(entryNombre.get()):
            nombre = entryNombre.get()
        else:
            labelError.config(text="!!El nombre solo debe tener \n caracteres alfanúmericos!!", bg="lightgray")
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        fecha = entryFecha.get_date()

        if vl.validarParticipantes(entryParticipantes.get()):
            participantes = entryParticipantes.get()
        else:
            labelError.config(text="!!La cantidad de participantes debe ser \n un numero entero mayor a 0 y menor a 1000", bg="lightgray")
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if checkValor.get() == 1:
            invitados = True
        else:
            invitados = False

        if vl.validarDescripcion(entryDescripcion.get()):
            descripcion = entryDescripcion.get()
        else:
            labelError.config(text="!!La descripción no debe exceder \n los 15 caracteres!!", bg="lightgray")
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        respuesta = bd.crearTablaAntesTorneo(nombre, fecha, participantes, invitados, descripcion)
        if respuesta == True:
            labelError.config(text="!!Ya existe un torneo con estos \n datos por favor ingrese uno nuevo!!", bg="lightgray")
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        labelError.config(text=f"!!Torneo creado con exito \n {respuesta}!!", bg="lightgray")

    #Ventana
    ventana = tk.Tk()
    ventana.title("Torneo")
    ventana.geometry("1000x500")
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

    labelInvitados = tk.Label(frame, text="Invitados", font= 20)
    labelInvitados.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelDescripcion = tk.Label(frame, text="Descripción", font= 20)
    labelDescripcion.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    entryNombre = tk.Entry(frame)
    entryNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    entryFecha = DateEntry(frame, date_pattern='dd-mm-yy', bg="gray", font=15, state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    entryParticipantes = tk.Entry(frame)
    entryParticipantes.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    checkValor = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValor, onvalue=1, offvalue=0)
    checkInvitados.grid(row=3, column=1, padx=10, pady=10)

    entryDescripcion = tk.Entry(frame)
    entryDescripcion.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=lambda: [entryNombre.delete(0, tk.END), 
                                                                     entryParticipantes.delete(0, tk.END), 
                                                                     entryFecha.config(state="normal"),
                                                                     entryFecha.delete(0, tk.END), 
                                                                     entryFecha.config(state="readonly"),
                                                                     checkInvitados.deselect(), 
                                                                     entryDescripcion.delete(0, tk.END)])
    botonLimpiar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    botonCrear = tk.Button(frame, text="Crear", font=20,  command=crearTorneo)
    botonCrear.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", font= 15, bg="gray")
    labelError.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        
    ventana.mainloop()
def crearTorneo():
    pass

def editarTorneo():
    pass

def borrarTorneo():
    pass

def filtrarTorneos():
    pass

interfazTorneo()

#5to poder
#El nombre de la rosa
#Farenheit 451 1966/2018