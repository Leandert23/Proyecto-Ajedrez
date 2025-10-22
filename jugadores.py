import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkinter import ttk, messagebox


def interfazJugadores1(ventanaMain):
    #Funciones
    def cargarJugadores():
        datos = bd.consultarDatosJugadores()
        labelJugadores.config(text=f"Jugadores:{len(datos)}")
        for registro in datos:
            nombreCompleto = registro[0]
            #if len(nombreCompleto) > 20:
                #nombreCompleto = nombreCompleto[:15] + "..."
            tabla.insert("", tk.END, values=(nombreCompleto, registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]))
        
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    """   def actualizarLista():
        print("Actualizando lista de jugadores...")
        for dato in tabla.get_children():
            tabla.delete(dato)
        cargarJugadores()"""
    def menu(event):
        fila = tabla.identify_row(event.y)
        if fila:
            menu.tk_popup(event.x_root, event.y_root)
    
    def editarFila():
        fila = tabla.selection()
        datos = tabla.item(fila, 'values')
        ventanaJugadores1.destroy()
        interfazJugadores4(ventanaMain, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])

    def borrarFila():
        item = tabla.selection()
        valores = tabla.item(item, 'values')
        respuesta = messagebox.askyesno("Borrar", f"¿Estás seguro de borrar a {valores[0]}?")
        if respuesta:
            tabla.delete(item)
            bd.eliminarDatosJugador(valores[0])
            cargarJugadores()
            
    #Ventana
    ventanaJugadores1 = tk.Toplevel(ventanaMain)
    ventanaJugadores1.title("Jugadores")
    anchoVentana = 700
    altoVentana = 400
    x = (ventanaJugadores1.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaJugadores1.winfo_screenheight() - altoVentana)//2
    ventanaJugadores1.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaMain.withdraw()
    ventanaJugadores1.focus_force()
    ventanaJugadores1.grab_set()
    ventanaJugadores1.resizable(False, False)
    ventanaJugadores1.configure(bg="lightgray")

    #Widgets
    labelTitulo = tk.Label(ventanaJugadores1, text=f"Jugadores", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaJugadores1, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido", "Género", "Facultad", "Elo", "Victorias", "Torneos", "Invitado"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")
    tabla.bind("<Button-3>", menu)

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

    menu = tk.Menu(ventanaJugadores1, tearoff=0)
    menu.add_command(label="Editar", command=editarFila)
    menu.add_command(label="Borrar", command=borrarFila)    
    
    labelJugadores = tk.Label(ventanaJugadores1, text="Jugadores:", bg="lightgray", fg="black", font=15)
    labelJugadores.pack(padx=10, pady=10, side=tk.LEFT)

    #botonBuscarJugador = tk.Button(ventanaJugadores1, text="Buscar Jugador", font=15, command=lambda: interfazJugadores3())
    #botonBuscarJugador.pack(padx=10, pady=10, side=tk.RIGHT)

    botonCrearJugador = tk.Button(ventanaJugadores1, text="Crear Jugador", font=15, command=lambda:(ventanaJugadores1.destroy(), interfazJugadores2(ventanaMain)))
    botonCrearJugador.pack(padx=10, pady=10, side=tk.RIGHT)

    cargarJugadores()

def interfazJugadores2(ventanaMain):
    #Funciones
    def crearJugador():
        if checkValorInvitado.get() == 1:
            invitado = "Si"
        else:
            invitado = "No"

        if vl.validarNombre(entryNombreCompleto.get()) and len(entryNombreCompleto.get()) <= 20:
            nombreCompleto = entryNombreCompleto.get()
        else:
            labelError.config(text="!!El nombre solo debe tener caracteres \n alfanúmericos, (Maximo 20 caracteres)!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarTexto(entryGenero.get()) and entryGenero.get().strip() != "":
            genero = entryGenero.get()
        else:
            labelError.config(text="!!El género solo debe tener caracteres \n alfanúmericos, (Maximo 15 caraceteres)!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarTexto(entryFacultad.get()) and entryFacultad.get().strip() != "":
            facultad = entryFacultad.get()
        else:
            labelError.config(text="!!La facultad solo debe tener caracteres \n alfanúmericos, (Maximo 15 caraceteres)!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
    
        if vl.validarEntero(entryElo.get()) and len(vl.validarEntero2(entryElo.get())) == 4:
            elo = entryElo.get()
        else:
            labelError.config(text="!!El elo debe ser un numero \n entero positivo de 4 dígitos", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarEntero(entryVictorias.get()) and len(vl.validarEntero2(entryVictorias.get())) <= 2:
            victorias = entryVictorias.get()
        else:
            labelError.config(text="!!El número de victorias debe ser un numero \n entero positivo de maximo 2 dígitos", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarEntero(entryTorneos.get()) and len(vl.validarEntero2(entryTorneos.get())) <= 2:
            torneos = entryTorneos.get()
        else:
            labelError.config(text="!!El número de torneos debe ser un numero \n entero positivo de maximo 2 dígitos", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        respuesta = bd.agregarDatosJugadores(nombreCompleto, genero, facultad, elo, victorias, torneos, invitado)
        if respuesta == True:
            labelError.config(text="!!Ya existe un Jugador con estos datos \n por favor ingrese uno nuevo!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        labelError.config(text=f"!!Jugador creado con exito \n {respuesta}!!", bg="lightgray", font=12)
        ventanaJugadores2.destroy()
        labelError.after(2000, lambda:interfazJugadores1(ventanaMain))

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
    ventanaJugadores2 = tk.Toplevel(ventanaMain)
    ventanaJugadores2.title("Jugadores")
    anchoVentana = 400
    altoVentana = 500
    x = (ventanaJugadores2.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaJugadores2.winfo_screenheight() - altoVentana)//2
    ventanaJugadores2.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaJugadores2.resizable(False, False)
    ventanaMain.withdraw()
    ventanaJugadores2.focus_force()
    ventanaJugadores2.grab_set()
    ventanaJugadores2.configure(bg="lightgray")
    ventanaJugadores2.bind("<Escape>", lambda e:(ventanaJugadores2.destroy(), interfazJugadores1(ventanaMain)))

    #Widgets
    labelTitulo = tk.Label(ventanaJugadores2, text="Agregar Jugador", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaJugadores2, bd=10, bg="gray", width=500, height=500)
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

    botonAgregar = tk.Button(frame, text="Agregar", font=20,  command=crearJugador)
    botonAgregar.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

"""
def interfazJugadores3():
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
            for i in listaJugadoresFiltrados:
                listaJugadores.insert(tk.END, i)


            #if len(nombreCompleto) > 20:
                #nombreCompleto = nombreCompleto[:15] + "..."
            #tabla.insert("", tk.END, values=(nombreCompleto, registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]))
        
        #if len(datos) > 10:
            #scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            #tabla.configure(yscroll=scrollbar.set)
            #scrollbar.grid(row=0, column=6, sticky="ns")


    #Ventana
    ventana = tk.Tk()
    ventana.title("Jugadores")
    anchoVentana = 400
    altoVentana = 300
    x = (ventana.winfo_screenwidth() - anchoVentana)//2
    seleccionarJugador = (ventana.winfo_screenheight() - altoVentana)//2
    ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{seleccionarJugador}")
    ventana.resizable(False, False)
    ventana.configure(bg="lightgray")
    #Widgets
    frame = tk.Frame(ventana, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    def seleccionarJugador(evento):
        indice = listaJugadores.curselection()
        elemento = listaJugadores.get(indice)
        ventana.destroy()

        
    listaJugadores = tk.Listbox(frame)
    listaJugadores.pack(padx=10, pady=10)
    listaJugadores.bind("<Double-Button-1>", seleccionarJugador)

    entryBusqueda = tk.Entry(frame, font=20)
    entryBusqueda.pack(padx=10, pady=10)
    entryBusqueda.focus()
    entryBusqueda.bind("<Key>", filtrarJugadores, add="+")
    entryBusqueda.bind("<BackSpace>", filtrarJugadores)    def hola(event):
        

    entryNombre.bind("<Key>", hola)
    entryFecha = DateEntry(frame, date_pattern='dd-mm-yy', bg="gray", font=20, state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    ventana.mainloop
"""
def interfazJugadores4(ventanaMain, nombreJugador, gen, fac, el, vict, torn, inv):
    #Funciones
    def datos():
        entryNombreCompleto.insert(0, nombreJugador)
        entryGenero.insert(0, gen)
        entryFacultad.insert(0, fac)
        entryElo.insert(0, el)
        entryVictorias.insert(0, vict)
        entryTorneos.insert(0, torn)
        if inv == "Si":
            checkValorInvitado.set(1)
        
    def editarJugador():
        if checkValorInvitado.get() == 1:
            invitado = "Si"
        else:
            invitado = "No"

        if vl.validarNombre(entryNombreCompleto.get()) and len(entryNombreCompleto.get()) <= 20:
            nombreCompleto = entryNombreCompleto.get()
        else:
            labelError.config(text="!!El nombre solo debe tener caracteres \n alfanúmericos, (Maximo 20 caracteres)!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarTexto(entryGenero.get()) and entryGenero.get().strip() != "":
            genero = entryGenero.get()
        else:
            labelError.config(text="!!El género solo debe tener caracteres \n alfanúmericos, (Maximo 15 caraceteres)!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarTexto(entryFacultad.get()) and entryFacultad.get().strip() != "":
            facultad = entryFacultad.get()
        else:
            labelError.config(text="!!La facultad solo debe tener caracteres \n alfanúmericos, (Maximo 15 caraceteres)!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
    
        if vl.validarEntero(entryElo.get()) and len(vl.validarEntero2(entryElo.get())) == 4:
            elo = entryElo.get()
        else:
            labelError.config(text="!!El elo debe ser un numero \n entero positivo de 4 dígitos", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarEntero(entryVictorias.get()) and len(vl.validarEntero2(entryVictorias.get())) <= 2:
            victorias = entryVictorias.get()
        else:
            labelError.config(text="!!El número de victorias debe ser un numero \n entero positivo de maximo 2 dígitos", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarEntero(entryTorneos.get()) and len(vl.validarEntero2(entryTorneos.get())) <= 2:
            torneos = entryTorneos.get()
        else:
            labelError.config(text="!!El número de torneos debe ser un numero \n entero positivo de maximo 2 dígitos", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        invitado = "Si" if checkValorInvitado.get() == 1 else "No"

        bd.actualizarDatosJugador(nombreCompleto, genero, facultad, elo, victorias, torneos, invitado)
        ventanaJugador4.destroy()
        interfazJugadores1(ventanaMain)

    #Ventana
    ventanaJugador4 = tk.Toplevel(ventanaMain)
    ventanaJugador4.title("Jugadores")
    anchoVentana = 400
    altoVentana = 500
    x = (ventanaJugador4.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaJugador4.winfo_screenheight() - altoVentana)//2
    ventanaJugador4.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaJugador4.resizable(False, False)
    ventanaMain.withdraw()
    ventanaJugador4.focus_force()
    ventanaJugador4.grab_set()
    ventanaJugador4.configure(bg="lightgray")
    ventanaJugador4.bind("<Escape>", lambda e:(ventanaJugador4.destroy(), interfazJugadores1(ventanaMain)))

    #Widgets
    labelTitulo = tk.Label(ventanaJugador4, text="EditarJugador", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaJugador4, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelNombre = tk.Label(frame, text="Nombre Completo", font= 20)
    labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelGenero = tk.Label(frame, text="Género", font= 20)
    labelGenero.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelFacultad = tk.Label(frame, text="Facultad", font= 20)
    labelFacultad.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelElo = tk.Label(frame, text="Elo", font= 20)
    labelElo.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelVictorias = tk.Label(frame, text="Victorias", font= 20)
    labelVictorias.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    labelTorneos = tk.Label(frame, text="Torneos", font= 20)
    labelTorneos.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    labelInvitado = tk.Label(frame, text="Invitado", font= 20)
    labelInvitado.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    entryNombreCompleto = tk.Entry(frame, font=20)
    entryNombreCompleto.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    entryGenero = tk.Entry(frame, font=20)
    entryGenero.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entryFacultad = tk.Entry(frame, font=20)
    entryFacultad.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entryElo = tk.Entry(frame, font=20)
    entryElo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entryVictorias = tk.Entry(frame, font=20)
    entryVictorias.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryTorneos = tk.Entry(frame, font=20)
    entryTorneos.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    checkValorInvitado = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValorInvitado, onvalue=1, offvalue=0, command=lambda:checkValorInvitado.get())
    checkInvitados.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=lambda: [entryNombreCompleto.delete(0, tk.END), entryGenero.delete(0, tk.END),
                                                                    entryFacultad.delete(0, tk.END), entryElo.delete(0, tk.END), 
                                                                    entryVictorias.delete(0, tk.END), entryNombreCompleto.focus()])
    botonLimpiar.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="Editar", font=20, command=editarJugador)
    botonEditar.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    datos()
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



