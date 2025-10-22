import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkcalendar import DateEntry
from tkinter import ttk, messagebox

#Interfaz1
def interfazTorneo1(ventanaMain):
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
        labelError.after(2000, lambda:(ventanaTorneo1.destroy(), interfazTorneo2(ventanaMain, respuesta, rondas)))

    #Ventana
    ventanaTorneo1 = tk.Toplevel(ventanaMain)
    ventanaTorneo1.title("Torneo")
    anchoVentana = 400
    altoVentana = 450
    x = (ventanaTorneo1.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo1.winfo_screenheight() - altoVentana)//2
    ventanaTorneo1.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo1.grab_set()
    ventanaTorneo1.focus_force()
    #ventanaMain.withdraw()
    ventanaTorneo1.resizable(False, False)
    ventanaTorneo1.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo1, text="Crear torneo", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaTorneo1, bd=10, bg="gray", width=500, height=500)
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

def interfazTorneo2(ventanaMain, nombreTorneo, rondas):
    #Funciones
    def actualizarTabla():
        for dato in tabla.get_children():
            tabla.delete(dato)
        datos = bd.consultarDatosTorneo(nombreTorneo)
        if len(datos) > 0:
            labelJugadoresInscritos.config(text=f"Jugadores inscritos: {len(datos)}")
        if not datos is None:
            for registro in datos:
                tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], f"{registro[8]}  {registro[9]}"))
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=10, sticky="ns")

    def menu(event):
        fila = tabla.identify_row(event.y)
        if fila:
            menu.tk_popup(event.x_root, event.y_root)
    
    def editarFila():
        fila = tabla.selection()
        datos = tabla.item(fila, 'values')
        ventanaTorneo2.destroy()
        interfazTorneo4(ventanaMain, nombreTorneo, datos[0], datos[4], datos[5], datos[6], datos[8], rondas)

    def borrarFila():
        item = tabla.selection()
        valores = tabla.item(item, 'values')
        respuesta = messagebox.askyesno("Borrar", f"¿Estás seguro de borrar a {valores[0]}?")
        if respuesta:
            tabla.delete(item)
            bd.eliminarJugadorTorneo(nombreTorneo, valores[0])
            actualizarTabla()

    #Ventana
    ventanaTorneo2 = tk.Toplevel(ventanaMain)
    ventanaTorneo2.title("Torneo")
    anchoVentana = 800
    altoVentana = 450
    x = (ventanaTorneo2.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo2.winfo_screenheight() - altoVentana)//2
    ventanaTorneo2.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    #ventanaMain.withdraw()
    ventanaTorneo2.focus_force()
    ventanaTorneo2.grab_set()
    ventanaTorneo2.resizable(False, False)
    ventanaTorneo2.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo2, text=f"{nombreTorneo}", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaTorneo2, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 15, rowheight=30)
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido", "Genero", "Facultad", "Elo", "Victorias", "Tablas", "Derrotas", "Puntos", "Desempates"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=9, padx=5, pady=10, sticky="ew")
    tabla.bind("<Button-3>", menu)

    #tabla.column("Posición", anchor=tk.CENTER, width=70)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Genero", anchor=tk.CENTER, width=60)
    tabla.column("Facultad", anchor=tk.CENTER, width=85)
    tabla.column("Elo", anchor=tk.CENTER, width=45)
    tabla.column("Victorias", anchor=tk.CENTER, width=70)
    tabla.column("Tablas", anchor=tk.CENTER, width=55)
    tabla.column("Derrotas", anchor=tk.CENTER, width=70)
    tabla.column("Puntos", anchor=tk.CENTER, width=60)
    tabla.column("Desempates", anchor=tk.CENTER, width=120)

    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Genero", text="Genero")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Elo", text="Elo")
    tabla.heading("Victorias", text="Victorias")
    tabla.heading("Tablas", text="Tablas")
    tabla.heading("Derrotas", text="Derrotas")
    tabla.heading("Puntos", text="Puntos")
    tabla.heading("Desempates", text="Desempates")

    menu = tk.Menu(ventanaTorneo2, tearoff=0)
    menu.add_command(label="Editar", command=editarFila)
    menu.add_command(label="Borrar", command=borrarFila)

    botonAgregarJugador = tk.Button(ventanaTorneo2, text="Agregar Jugador", font=15, command=lambda:(ventanaTorneo2.destroy(), interfazTorneo3(ventanaMain, nombreTorneo, rondas)))
    botonAgregarJugador.pack(padx=10, pady=10, side=tk.RIGHT)

    labelJugadoresInscritos = tk.Label(ventanaTorneo2, text="!!No hay jugadores inscritos!!", bg="lightgray", font=20)
    labelJugadoresInscritos.pack(padx=10, pady=10, side=tk.LEFT)
    
    labelRondas = tk.Label(ventanaTorneo2, text=f"Rondas: {rondas}", bg="lightgray", font=20)
    labelRondas.pack(padx=10, pady=10, side=tk.LEFT)

    actualizarTabla()

def interfazTorneo3(ventanaMain, nombreTorneo, rondas):
    #Funciones
    def filtrarJugadores(evento):
        datos = bd.consultarDatosJugadores()
        listaJugadoresFiltrados = []
        nombreCompletos = []
        for registro in datos:
            nombreCompletos.append(registro[0])
        for nombre in nombreCompletos:
            if entryBusqueda.get().lower() in nombre.lower():
                listaJugadoresFiltrados.append(nombre)
        listaJugadores.delete(0, tk.END)
        for jugador in listaJugadoresFiltrados:
            if len(jugador) > 20:
                jugador = jugador[:20] + "..."
            listaJugadores.insert(tk.END, jugador)

        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listaJugadores.yview)
            listaJugadores.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky="ns")
    
    def seleccionarJugador(evento):
        indice = listaJugadores.curselection()
        nombreJugador = listaJugadores.get(indice)
        bd.consultarDatosJugador(nombreJugador, nombreTorneo)
        ventanaTorneo3.destroy()
        interfazTorneo2(ventanaMain, nombreTorneo, rondas)  


    #Ventana
    ventanaTorneo3 = tk.Toplevel(ventanaMain)
    ventanaTorneo3.title("Jugadores")
    anchoVentana = 275
    altoVentana = 325
    x = (ventanaTorneo3.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo3.winfo_screenheight() - altoVentana)//2
    ventanaTorneo3.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo3.focus_force()
    ventanaTorneo3.grab_set()
    ventanaTorneo3.resizable(False, False)
    ventanaTorneo3.configure(bg="lightgray")
    ventanaTorneo3.bind("<Escape>", lambda e:(ventanaTorneo3.destroy(), interfazTorneo2(ventanaMain, nombreTorneo, rondas)))
    #Widgets
    labelAgregarJugador = tk.Label(ventanaTorneo3, text="Agregar Jugador", font=15)
    labelAgregarJugador.pack(padx=10, pady=10) 

    frame = tk.Frame(ventanaTorneo3, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)   
        
    listaJugadores = tk.Listbox(frame, width=15, height=10, font=20)
    listaJugadores.grid(row=0, column=0)
    x = listaJugadores.bind("<Double-Button-1>", seleccionarJugador)

    entryBusqueda = tk.Entry(frame, font=20)
    entryBusqueda.grid(row=1, padx=5, pady=10)
    entryBusqueda.focus()
    entryBusqueda.bind("<KeyRelease>", filtrarJugadores)

    filtrarJugadores(x)

def interfazTorneo4(ventanaMain, nombreTorneo, nombreJugador, vict, tabl, derro, desemp, rondas):
    #Funciones
    def datos():
        desempates = desemp.split("  ")
        entryVictorias.insert(0, vict)
        entryTablas.insert(0, tabl)
        entryDerrotas.insert(0, derro)
        entryDesempate1.insert(0, desempates[0])
        entryDesempate2.insert(0, desempates[1])

    def editarJugador():
        if vl.validarEntero(entryVictorias.get()):
            victorias = entryVictorias.get()
        else:
            labelError.config(text="!!El número de victorias debe ser \n un número entero positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarEntero(entryTablas.get()):
            tablas = entryTablas.get()
        else:
            labelError.config(text="!!El número de tablas debe ser \n un número entero positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
           
        if vl.validarEntero(entryDerrotas.get()):
            derrotas= entryDerrotas.get()
        else:
            labelError.config(text="!!El número de derrotas debe ser \n un numero entero positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarFloat(entryDesempate1.get()):
            desempate1 = entryDesempate1.get()
        else:
            labelError.config(text="!!El desempate debe ser \n un numero decimal positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarFloat((entryDesempate2.get())):
            desempate2 = entryDesempate2.get()
        else:
            labelError.config(text="!!El desempate debe ser \n un numero decimal positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        estadisticas = int(victorias) + int(tablas) + int(derrotas)
        if estadisticas != int(rondas):
            labelError.config(text=f"!!El número de victorias + tablas + derrotas \n debe ser igual al numero de rondas: [{rondas}]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        puntos = int(victorias) + int(tablas)/2
        bd.actualizarJugadorTorneo(nombreTorneo, nombreJugador, victorias, tablas, derrotas, puntos, round(float(desempate1),2), round(float(desempate2),2))
        ventanaTorneo4.destroy()
        interfazTorneo2(ventanaMain, nombreTorneo, rondas)

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
    ventanaTorneo4 = tk.Toplevel(ventanaMain)
    ventanaTorneo4.title("Jugadores")
    anchoVentana = 400
    altoVentana = 400
    x = (ventanaTorneo4.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo4.winfo_screenheight() - altoVentana)//2
    ventanaTorneo4.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo4.resizable(False, False)
    ventanaMain.withdraw()
    ventanaTorneo4.focus_force()
    ventanaTorneo4.grab_set()
    ventanaTorneo4.configure(bg="lightgray")
    ventanaTorneo4.bind("<Escape>", lambda e:(ventanaTorneo4.destroy(), interfazTorneo2(ventanaMain, nombreTorneo, rondas )))

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo4, text="EditarJugador", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaTorneo4, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelVictorias = tk.Label(frame, text="Victorias", font= 20)
    labelVictorias.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelTablas = tk.Label(frame, text="Tablas", font= 20)
    labelTablas.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelDerrotas = tk.Label(frame, text="Derrotas", font= 20)
    labelDerrotas.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelDesempate1 = tk.Label(frame, text="Desempate1", font= 20)
    labelDesempate1.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelDesempate2 = tk.Label(frame, text="Desempate2", font= 20)
    labelDesempate2.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    entryVictorias = tk.Entry(frame, font=20)
    entryVictorias.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    entryTablas = tk.Entry(frame, font=20)
    entryTablas.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entryDerrotas = tk.Entry(frame, font=20)
    entryDerrotas.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entryDesempate1 = tk.Entry(frame, font=20)
    entryDesempate1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entryDesempate2 = tk.Entry(frame, font=20)
    entryDesempate2.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=lambda: [entryVictorias.delete(0, tk.END), entryTablas.delete(0, tk.END),
                                                                    entryDerrotas.delete(0, tk.END), entryDesempate1.delete(0, tk.END), 
                                                                    entryDesempate2.delete(0, tk.END), entryVictorias.focus()])
    botonLimpiar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="Editar", font=20, command=editarJugador)
    botonEditar.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    datos()

def editarTorneo():
    pass

def borrarTorneo():
    pass

def filtrarTorneos():
    pass

#if __name__ == "__main__":
    #interfazTorneo1()
    #interfazTorneo2("Julio_2025/10/20_P12_R12_True_12", 12)
    #interfazTorneo3()

#5to poder
#El nombre de la rosa
#Farenheit 451 1966/2018