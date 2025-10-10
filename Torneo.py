import tkinter as tk

def interfazTorneo():
    def crearTorneo():
        torneo = []
        nombre = entryNombre.get()
        participantes = entryParticipantes.get()
        fecha = entryFecha.get()
        invitados = entryInvitados.get()
        descripcion = entryDescripcion.get()
        torneo.append(nombre)
        torneo.append(participantes)
        torneo.append(fecha)
        torneo.append(invitados)
        torneo.append(descripcion)
        print(torneo)
    ventana = tk.Tk()
    ventana.title("Torneo")
    ventana.geometry("1000x600")
    ventana.configure(bg="lightgray")

    labelTitulo = tk.Label(ventana, text="Crear torneo", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventana, bd=10, bg="gray", width=500, height=500)
    #frame.pack(pady=10, ipadx=250, ipady=250)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelNombre = tk.Label(frame, text="Nombre", font= 20)
    labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelParticipantes = tk.Label(frame, text="Participantes", font= 20)
    labelParticipantes.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelFecha = tk.Label(frame, text="Fecha", font= 20)
    labelFecha.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelInvitados = tk.Label(frame, text="Invitados", font= 20)
    labelInvitados.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelDescripcion = tk.Label(frame, text="Descripción", font= 20)
    labelDescripcion.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    entryNombre = tk.Entry(frame)
    entryNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    entryParticipantes = tk.Entry(frame)
    entryParticipantes.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entryFecha = tk.Entry(frame)
    entryFecha.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entryInvitados = tk.Entry(frame)
    entryInvitados.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame)
    entryDescripcion.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=lambda: [entryNombre.delete(0, tk.END), 
                                                                     entryParticipantes.delete(0, tk.END), 
                                                                     entryFecha.delete(0, tk.END), 
                                                                     entryInvitados.delete(0, tk.END), 
                                                                     entryDescripcion.delete(0, tk.END)])
    botonLimpiar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    botonCrear = tk.Button(frame, text="Crear", font=20,  command=crearTorneo)
    botonCrear.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        
    ventana.mainloop()

def crearTorneo():
    pass

def editarTorneo():
    pass

def borrarTorneo():
    pass

def filtrarTorneos():
    pass

#interfazTorneo()

#5to poder
#El nombre de la rosa
#Farenheit 451 1966/2018