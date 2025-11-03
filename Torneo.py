import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkcalendar import DateEntry
from tkinter import ttk, messagebox
import sys

#Interfaz1
def interfazTorneo1(ventanaMain):
    #Funciones
    def crearTorneo():
        if vl.validarNombre(entryNombre.get()):
            nombre = entryNombre.get()
        else:
            labelError.config(text="!!El nombre solo debe tener caracteres \n alfanúmericos [Máximo 15]!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        fecha = entryFecha.get_date()

        if vl.validarEntero(spinboxParticipantes.get()):
            participantes = spinboxParticipantes.get()
        else:
            labelError.config(text="!!La cantidad de participantes debe ser \n un numero entero mayor a 0 y menor a 100", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarEntero(spinboxRondas.get()):
            rondas = spinboxRondas.get()
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
        labelError.config(text=f"!!Torneo creado con exito \n {nombre}!!", bg="lightgray", font=12)
        datosTorneo = (nombre, fecha, participantes, rondas, invitados, descripcion)
        labelError.after(2000, lambda:(ventanaTorneo1.destroy(), interfazTorneo2(ventanaMain, respuesta, datosTorneo)))

    def limpiar():
        entryNombre.delete(0, tk.END)
        spinboxParticipantes.delete(0, tk.END)
        spinboxRondas.delete(0, tk.END)
        entryFecha.config(state="normal")
        entryFecha.set_date(None)
        entryFecha.config(state="readonly")
        checkInvitados.deselect()
        entryDescripcion.delete(0, tk.END)
        entryNombre.focus()

    #Ventana
    ventanaTorneo1 = tk.Toplevel(ventanaMain)
    ventanaTorneo1.title("Torneo")
    anchoVentana = 400
    altoVentana = 450
    x = (ventanaTorneo1.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo1.winfo_screenheight() - altoVentana)//2
    ventanaTorneo1.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo1.focus_force()
    ventanaTorneo1.grab_set()
    ventanaTorneo1.resizable(False, False)
    ventanaTorneo1.configure(bg="lightgray")
    ventanaTorneo1.bind("<Escape>", lambda e:(ventanaMain.deiconify(), ventanaTorneo1.destroy()))
    ventanaTorneo1.bind("<Return>", lambda e: crearTorneo())
    ventanaTorneo1.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo1.destroy(), sys.exit(0)))

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
    ventanaTorneo1.after(10, lambda:entryNombre.focus())

    entryFecha = DateEntry(frame, date_pattern='dd-mm-yy', bg="gray", font=20, state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    spinboxParticipantes = tk.Spinbox(frame, from_=1, to=100, font=20)
    spinboxParticipantes.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxRondas = tk.Spinbox(frame, from_=1, to=100, font=20)
    spinboxRondas.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    checkValor = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValor, onvalue=1, offvalue=0)
    checkInvitados.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame, font=20)
    entryDescripcion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=limpiar)
    botonLimpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    botonCrear = tk.Button(frame, text="Crear", font=20,  command=crearTorneo)
    botonCrear.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

def interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo):
    #Funciones
    def actualizarTabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosAntesTorneo(nombreTorneo)

        if len(datos) > 0:
            labelJugadoresInscritos.config(text=f"Jugadores inscritos: {len(datos)}/{datosTorneo[2]}")
        else:
            labelJugadoresInscritos.config(text=f"Jugadores inscritos: 0/{datosTorneo[2]}")
            return
        
        if not datos is None:
            for registro in datos:
                tag = ""
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

                if registro[4] == "0":
                    victorias = "0"
                else:
                    victorias = registro[4]

                if registro[5] == "0":
                    tablas = "0"
                else:
                    tablas = registro[5]
                
                if registro[6] == "0":
                    derrotas = "0"
                else:
                    derrotas = registro[6]
                
                
                tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], victorias , tablas, derrotas, registro[7], (f"{registro[8]}  {registro[9]}"), registro[10]), tags=(tag))
                
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=10, sticky="ns")

    def menu(evento):
        fila = tabla.identify_row(evento.y)
        if fila:
            tabla.selection_set(fila)
            menu.tk_popup(evento.x_root, evento.y_root)
    
    def editarFila():
        fila = tabla.selection()
        datos = tabla.item(fila, 'values')
        ventanaTorneo2.withdraw()
        interfazTorneo4(ventanaMain, nombreTorneo, datos[0], datos[4], datos[5], datos[6], datos[8], datosTorneo)

    def borrarFila():
        item = tabla.selection()
        valores = tabla.item(item, 'values')
        respuesta = messagebox.askyesno("Borrar", f"¿Estás seguro de borrar a {valores[0]}?")
        if respuesta:
            tabla.delete(item)
            bd.eliminarJugadorTorneo(nombreTorneo, valores[0]) 
            actualizarTabla()

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)

    def cargarTorneo():
        jugadoresInscritos = []
        estadisticasJugadores = []
        desempatesJugadores = []
        invitado = False
        for fila in tabla.get_children():
            valores = tabla.item(fila, 'values')
            if valores[4] == "0":
                victorias = 0
            else:
                victorias = len((valores[4])[2:-1])
            
            datos = valores[0], valores[2]
            estadisticas = valores[0], victorias, valores[9]
            desempates = valores[8].split("  ")
            desempate = valores[7], desempates[0], desempates[1]
            jugadoresInscritos.append(datos)
            estadisticasJugadores.append(estadisticas)
            desempatesJugadores.append(desempate)
            #Nombre, Genero, Facultad, Elo, Victorias, Tablas, Derrotas, Puntos, Desempates, diferenciaElo

        respuesta = messagebox.askyesno("Cargar", "¿Estás seguro de cargar el torneo? \n ¡!Una vez cargado no se podrá editar el torneo!!")
        if respuesta:
            if len(jugadoresInscritos) != int(datosTorneo[2]):
                messagebox.showerror("Error", f"!!Debe haber {datosTorneo[2]} jugador/es \n inscritos para cargar el torneo!!")
                return
            for jugadores in jugadoresInscritos:
                if jugadores[1] == "Invitado":
                    invitado = True
            if invitado and datosTorneo[4] == "False":
                messagebox.showerror("Error", "!!No se permiten invitados en este torneo!!")
                return
            if invitado == False and datosTorneo[4] == "True":
                messagebox.showerror("Error", "!!Debe haber al menos un invitado en este torneo!!")
                return
        
            respuesta = bd.crearTablaDespuesTorneo(datosTorneo[0], datosTorneo[1], datosTorneo[2], datosTorneo[3], datosTorneo[4], datosTorneo[5])
            i = 0
            for jugadores in jugadoresInscritos:
                bd.consultarDatosJugador(respuesta, jugadores[0], desempatesJugadores[i])
                i += 1
            messagebox.showinfo("Torneo", "!!Torneo cargado con exito!!")
            ventanaTorneo2.destroy()
            interfazTorneo6(ventanaMain, respuesta, datosTorneo, estadisticasJugadores)

    def eliminarTabla():
        bd.eliminarTabla(nombreTorneo)
    #Ventana
    ventanaTorneo2 = tk.Toplevel(ventanaMain)
    ventanaTorneo2.title("Torneo")
    anchoVentana = 850
    altoVentana = 450
    x = (ventanaTorneo2.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo2.winfo_screenheight() - altoVentana)//2
    ventanaTorneo2.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo2.focus_force()
    ventanaTorneo2.grab_set()
    ventanaTorneo2.resizable(False, False)
    ventanaTorneo2.configure(bg="lightgray")
    ventanaTorneo2.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaTorneo2.bind("<Return>", lambda e: cargarTorneo())
    ventanaTorneo2.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo2.destroy(), eliminarTabla(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo2, text=f"{datosTorneo[0]}", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaTorneo2, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 15, rowheight=30)
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido", "Genero", "Facultad", "Elo", "Victorias", "Tablas", "Derrotas", "Puntos", "Desempates", "Diferencia Elo"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=9, padx=5, pady=10, sticky="ew") 
    tabla.bind("<Button-3>", menu)

    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=180)
    tabla.column("Genero", anchor=tk.CENTER, width=60)
    tabla.column("Facultad", anchor=tk.CENTER, width=95)
    tabla.column("Elo", anchor=tk.CENTER, width=45)
    tabla.column("Victorias", anchor=tk.CENTER, width=75)
    tabla.column("Tablas", anchor=tk.CENTER, width=75)
    tabla.column("Derrotas", anchor=tk.CENTER, width=75)
    tabla.column("Puntos", anchor=tk.CENTER, width=60)
    tabla.column("Desempates", anchor=tk.CENTER, width=100)
    tabla.column("Diferencia Elo", anchor=tk.CENTER, width=0, stretch=False, minwidth=0)
    
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

    botonAgregarJugador = tk.Button(ventanaTorneo2, text="Agregar Jugador", font=15, command=lambda:(ventanaTorneo2.withdraw(), interfazTorneo3(ventanaMain, nombreTorneo, datosTorneo)))
    botonAgregarJugador.pack(padx=10, pady=10, side=tk.RIGHT)

    botonContinuarTorneo = tk.Button(ventanaTorneo2, text="Continuar", font=15, command= cargarTorneo)
    botonContinuarTorneo.pack(padx=10, pady=10, side=tk.RIGHT)

    botonEditarTorneo = tk.Button(ventanaTorneo2, text="Editar", font=15, command= lambda:(ventanaTorneo2.withdraw(), interfazTorneo5(ventanaMain, nombreTorneo, datosTorneo)))
    botonEditarTorneo.pack(padx=10, pady=10, side=tk.RIGHT)


    labelJugadoresInscritos = tk.Label(ventanaTorneo2, text=f"Jugadores inscritos: 0/{datosTorneo[2]}", bg="lightgray", font=20)
    labelJugadoresInscritos.pack(padx=10, pady=10, side=tk.LEFT)
    
    labelRondas = tk.Label(ventanaTorneo2, text=f"Rondas: {datosTorneo[3]} ", bg="lightgray", font=20)
    labelRondas.pack(padx=10, pady=10, side=tk.LEFT)

    labelInvitados = tk.Label(ventanaTorneo2, text=f"Invitados: {"Si" if datosTorneo[4] == "True" else "No"}", bg="lightgray", font=20)
    labelInvitados.pack(padx=10, pady=10, side=tk.LEFT)

    actualizarTabla()

def interfazTorneo3(ventanaMain, nombreTorneo, datosTorneo):
    #Funciones
    def filtrarJugadores():
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
            listaJugadores.insert(tk.END, jugador)

        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listaJugadores.yview)
            listaJugadores.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky="ns")
    
    def seleccionarJugador():
        indice = listaJugadores.curselection()
        nombreJugador = listaJugadores.get(indice)
        respuesta = bd.consultarDatosJugador(nombreTorneo, nombreJugador, True)
        if respuesta == True:
            labelError.config(text="!!Ya existe un Jugador inscrito \n con estos datos por favor \n ingrese uno diferente!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        ventanaTorneo3.destroy()
        interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo)  

    #Ventana
    ventanaTorneo3 = tk.Toplevel(ventanaMain)
    ventanaTorneo3.title("Jugadores")
    anchoVentana = 300
    altoVentana = 400
    x = (ventanaTorneo3.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo3.winfo_screenheight() - altoVentana)//2
    ventanaTorneo3.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo3.focus_force()
    ventanaTorneo3.grab_set()
    ventanaTorneo3.resizable(False, False)
    ventanaTorneo3.configure(bg="lightgray")
    ventanaTorneo3.bind("<Escape>", lambda e:(ventanaTorneo3.destroy(), interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo)))
    ventanaTorneo3.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo3.destroy(), sys.exit(0)))

    #Widgets
    labelAgregarJugador = tk.Label(ventanaTorneo3, text="Agregar Jugador", font=15)
    labelAgregarJugador.pack(padx=10, pady=10) 

    frame = tk.Frame(ventanaTorneo3, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)   
        
    listaJugadores = tk.Listbox(frame, width=20, height=10, font=20)
    listaJugadores.grid(row=0, column=0, sticky="ew")
    listaJugadores.bind("<Double-Button-1>", lambda e:seleccionarJugador())

    entryBusqueda = tk.Entry(frame, font=20)
    entryBusqueda.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    ventanaTorneo3.after(100, lambda:entryBusqueda.focus())
    entryBusqueda.bind("<KeyRelease>", lambda e:filtrarJugadores())

    labelError = tk.Label(frame, text="", bg="gray", font=10)
    labelError.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    filtrarJugadores()

def interfazTorneo4(ventanaMain, nombreTorneo, nombreJugador, vict, tabl, derro, desemp, datosTorneo):
    #Funciones
    def insertarDatos():
        desempates = desemp.split("  ")
        entryVictorias.insert(0,f"{vict[2:-1] if vict != "0" else "0"}")
        entryTablas.insert(0, f"{tabl[2:-1] if tabl != "0" else "0"}")
        entryDerrotas.insert(0, f"{derro[2:-1] if derro != "0" else "0"}")
        spinboxDesempate1.delete(0, tk.END)
        spinboxDesempate2.delete(0, tk.END)
        spinboxDesempate1.insert(0, desempates[0])
        spinboxDesempate2.insert(0, desempates[1])

    def editarJugador():
        eloVictorias = vl.validarEloVictorias(entryVictorias.get())
        numeroVictorias = len(entryVictorias.get())
        if eloVictorias == "False":
            labelError.config(text="!!Simbolo incorrecto (Victorias) \n Permitidos [+, -, =]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        if entryVictorias.get() == "0":
            numeroVictorias = 0
        
        eloTablas = vl.validarEloTablas(entryTablas.get())
        numeroTablas = len(entryTablas.get())
        if eloTablas == "False":
            labelError.config(text="!!Simbolo incorrecto (Tablas) \n Permitidos [+, -]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        if entryTablas.get() == "0":
            numeroTablas = 0
        
        eloDerrotas = vl.validarEloDerrotas(entryDerrotas.get())
        numeroDerrotas = len(entryDerrotas.get())
        if eloDerrotas == "False":
            labelError.config(text="!!Simbolo incorrecto (Derrotas) \n Permitidos [+, -, =]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        if entryDerrotas.get() == "0":
            numeroDerrotas = 0
        
        if vl.validarFloat(spinboxDesempate1.get()):
            desempate1 = spinboxDesempate1.get()
        else:
            labelError.config(text="!!El desempate debe ser \n un numero decimal positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if vl.validarFloat((spinboxDesempate2.get())):
            desempate2 = spinboxDesempate2.get()
        else:
            labelError.config(text="!!El desempate debe ser \n un numero decimal positivo!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        estadisticas = numeroVictorias + numeroTablas + numeroDerrotas
        diferenciaElo = eloVictorias + eloTablas + eloDerrotas
        if estadisticas != int(datosTorneo[3]):
            labelError.config(text=f"!!La cantidad de victorias + tablas + derrotas \n debe ser igual al numero de rondas: [{datosTorneo[3]}]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if numeroVictorias == 0:
            victorias = "0"
        else:
            victorias = f"{numeroVictorias}({entryVictorias.get()})"

        if numeroTablas == 0:
            tablas = "0"
        else:
            tablas = f"{numeroTablas}({entryTablas.get()})"
        
        if numeroDerrotas == 0:
            derrotas= "0"
        else:
            derrotas = f"{numeroDerrotas}({entryDerrotas.get()})"

        puntos = int(numeroVictorias) + int(numeroTablas)/2
        bd.actualizarJugadorTorneo(nombreTorneo, nombreJugador, victorias, tablas, derrotas, puntos, round(float(desempate1),2), round(float(desempate2),2), diferenciaElo)
        ventanaTorneo4.destroy()
        interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo)

    def limpiar():
        entryVictorias.delete(0, tk.END)
        entryTablas.delete(0, tk.END)
        entryDerrotas.delete(0, tk.END)
        spinboxDesempate1.delete(0, tk.END)
        spinboxDesempate2.delete(0, tk.END) 
        entryVictorias.focus()

    #Ventana
    ventanaTorneo4 = tk.Toplevel(ventanaMain)
    ventanaTorneo4.title("Jugadores")
    anchoVentana = 400
    altoVentana = 425
    x = (ventanaTorneo4.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo4.winfo_screenheight() - altoVentana)//2
    ventanaTorneo4.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo4.resizable(False, False)
    ventanaTorneo4.focus_force()
    ventanaTorneo4.grab_set()
    ventanaTorneo4.configure(bg="lightgray")
    ventanaTorneo4.bind("<Escape>", lambda e:(ventanaTorneo4.destroy(), interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo)))
    ventanaTorneo4.bind("<Return>", lambda e: editarJugador())
    ventanaTorneo4.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo4.destroy(), sys.exit(0)))

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
    ventanaTorneo4.after(10, lambda:entryVictorias.focus())

    entryTablas = tk.Entry(frame, font=20)
    entryTablas.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entryDerrotas = tk.Entry(frame, font=20)
    entryDerrotas.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxDesempate1 = tk.Spinbox(frame, from_=0.00, to=99.00, increment=0.5, format="%.2f", font=20)
    spinboxDesempate1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    spinboxDesempate2 = tk.Spinbox(frame, from_=0.00, to=99.00, increment=0.5, format="%.2f", font=20)
    spinboxDesempate2.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=limpiar)
    botonLimpiar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="Editar", font=20, command=editarJugador)
    botonEditar.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    insertarDatos()

def interfazTorneo5(ventanaMain, nombreTorneo, datosTorneo):
    #Funciones
    #(nombre, fecha, participantes, rondas, invitados, descripcion)
    def insertarDatos():
        entryNombre.insert(0, datosTorneo[0])
        entryFecha.insert(0, datosTorneo[1])
        spinboxParticipantes.delete(0, tk.END)
        spinboxRondas.delete(0, tk.END)
        spinboxParticipantes.insert(0, datosTorneo[2])
        spinboxRondas.insert(0, datosTorneo[3])
        if datosTorneo[4] == "True":
            checkValor.set(1)
        entryDescripcion.insert(0, datosTorneo[5])

    def editarTorneo():
        if vl.validarNombre(entryNombre.get()):
            nombre = entryNombre.get()
        else:
            labelError.config(text="!!El nombre solo debe tener \n caracteres alfanúmericos!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        fecha = entryFecha.get_date()

        if vl.validarEntero(spinboxParticipantes.get()):
            participantes = spinboxParticipantes.get()
        else:
            labelError.config(text="!!La cantidad de participantes debe ser \n un numero entero mayor a 0 y menor a 100", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarEntero(spinboxRondas.get()):
            rondas = spinboxRondas.get()
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
        
        respuesta = bd.actualizarAntesTorneo(nombreTorneo, nombre, fecha, participantes, rondas, invitados, descripcion)
        if respuesta == True:
            labelError.config(text="!!Ya existe un torneo con estos datos \n por favor ingrese uno nuevo!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        labelError.config(text=f"!!Torneo editado con exito!!", bg="lightgray", font=12)
        datosTorneo = (nombre, fecha, participantes, rondas, invitados, descripcion)
        labelError.after(2000, lambda:(ventanaTorneo5.destroy(), interfazTorneo2(ventanaMain, respuesta, datosTorneo)))

    def limpiar():
        entryNombre.delete(0, tk.END)
        spinboxParticipantes.delete(0, tk.END)
        spinboxRondas.delete(0, tk.END)
        entryFecha.config(state="normal")
        entryFecha.set_date(None)
        entryFecha.config(state="readonly")
        checkInvitados.deselect()
        entryDescripcion.delete(0, tk.END)
        entryNombre.focus()

    #Ventana
    ventanaTorneo5 = tk.Toplevel(ventanaMain)
    ventanaTorneo5.title("Torneo")
    anchoVentana = 400
    altoVentana = 450
    x = (ventanaTorneo5.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo5.winfo_screenheight() - altoVentana)//2
    ventanaTorneo5.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo5.grab_set()
    ventanaTorneo5.focus_force()
    ventanaTorneo5.resizable(False, False)
    ventanaTorneo5.configure(bg="lightgray")
    ventanaTorneo5.bind("<Escape>", lambda e:(ventanaTorneo5.destroy(), interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo)))
    ventanaTorneo5.bind("<Return>", lambda e: editarTorneo())
    ventanaTorneo5.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo5.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo5, text="Editar torneo", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaTorneo5, bd=10, bg="gray", width=500, height=500)
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
    ventanaTorneo5.after(10, lambda:entryNombre.focus())

    entryFecha = DateEntry(frame, date_pattern='dd-mm-yy', bg="gray", font=20, state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    spinboxParticipantes = tk.Spinbox(frame, from_=1, to=100, font=20)
    spinboxParticipantes.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxRondas = tk.Spinbox(frame, from_=1, to=100, font=20)
    spinboxRondas.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    checkValor = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValor, onvalue=1, offvalue=0)
    checkInvitados.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame, font=20)
    entryDescripcion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=limpiar)
    botonLimpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="Editar", font=20,  command=editarTorneo)
    botonEditar.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    insertarDatos()

#[Nombre y Apellido], Facultad, Elo, Victorias, Torneos, Medallas
#diferenciaElo, Victorias
def interfazTorneo6(ventanaMain, nombreTorneo, datosTorneo, estadisticasJugadores):
    #Funciones
    def actualizarTabla():
        global posiciones
        for dato in tabla.get_children():
            tabla.delete(dato)
        datos = bd.consultarDatosDespuesTorneo(nombreTorneo)
        posiciones = 0
        femenino = True
        if not datos is None:
            for registro in datos:
                tag = ""
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
                tabla.tag_configure("Oro", background="#DEDE2C", foreground="#FFFFFF")
                tabla.tag_configure("Plata", background="#545050", foreground="#FFFFFF")
                tabla.tag_configure("Bronce", background="#8D4416", foreground="#FFFFFF")
                tabla.tag_configure("Femenina", background="#DE2C50", foreground="#FFFFFF")
                tabla.tag_configure("Ingeniería", background="#00008B", foreground="#FFFFFF")
                tabla.tag_configure("Sociales", background="#A52A2A", foreground="#FFFFFF")
                tabla.tag_configure("Arquitectura", background="#402169", foreground="#FFFFFF")
                tabla.tag_configure("Derecho", background="#000000", foreground="#FFFFFF")
                tabla.tag_configure("Odontología", background="#888888", foreground="#FFFFFF")
                tabla.tag_configure("Invitado", background="#73bf00", foreground="#FFFFFF")
                tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")

                encontrado = True
                for i in range(len(datos)):
                    if encontrado == True:
                        for nombre in estadisticasJugadores:
                            if nombre[0] == registro[0]:
                                indice = estadisticasJugadores.index(nombre)
                                encontrado = False
                                break
         
                participantes = len(datos) - posiciones
                                                        #       [Nombre y Apellido], Genero, Facultad,        Puntos,                Desempates,                                                                                              Elo,                                                                                     Victorias,                                 Medallas,                Torneos,
                if posiciones <= 2:
                    if posiciones == 0:
                        tag = "Oro"
                    elif posiciones == 1:
                        tag = "Plata"
                    else:
                        tag = "Bronce"
                    tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}(+{estadisticasJugadores[indice][1]})"), (f"{registro[5]}(+1)")), tags=(tag))
                    bd.actualizarDatosJugador(registro[0], (registro[3]+(int(estadisticasJugadores[indice][2])+participantes)), (int(registro[4])+int(estadisticasJugadores[indice][1])), (int(registro[6])+1), (int(registro[5])+1), tag)
                    posiciones += 1
                    participantes -= 1
                elif femenino == True and registro[1] == "F":
                    tag = "Femenina"
                    tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"),(f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}(+{estadisticasJugadores[indice][1]})"), (f"{registro[5]}(+1)")), tags=(tag))
                    bd.actualizarDatosJugador(registro[0], (registro[3]+(int(estadisticasJugadores[indice][2])+participantes)), (int(registro[4])+int(estadisticasJugadores[indice][1])), (int(registro[6])+1), (int(registro[5])+1), "Otra")
                    posiciones += 1
                    participantes -= 1
                    femenino = False
                else:
                    tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}(+{estadisticasJugadores[indice][1]})"), registro[5]), tags=(tag))
                    bd.actualizarDatosJugador(registro[0], (registro[3]+(int(estadisticasJugadores[indice][2])+participantes)), (int(registro[4])+int(estadisticasJugadores[indice][1])), (int(registro[6])+1), int(registro[5]))
                    posiciones += 1
                    participantes -= 1
                #tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], (f"{registro[3] + estadisticasJugadores[0]}"), (f"{registro[4] + estadisticasJugadores[1]}"),(f"{registro[5] + estadisticasJugadores[1]}")), tags=(tag))
                                            #"#", "Nombre y Apellido", "Genero", "Facultad", "Elo(+/-)", "Victorias(+)", "Medallas(+)"
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=10, sticky="ns")

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    def verDatos():
        messagebox.showinfo("Información Torneo:", f" Nombre: {datosTorneo[0]} \n Fecha: {datosTorneo[1]} \n Participantes: {datosTorneo[2]} \n Rondas: {datosTorneo[3]} \n Invitados: {"Si" if datosTorneo[4] == "True" else "No"} \n Descripción: {"Ninguna" if datosTorneo[5] == "" else datosTorneo[5]}")

    def guardarTorneo():
        bd.agregarDatosListaTorneos(datosTorneo[0], datosTorneo[1].replace("-", "/"), datosTorneo[2], datosTorneo[3], datosTorneo[4], (f"{"Ninguna" if datosTorneo[5] == "" else datosTorneo[5]}"))
    #Ventana
    ventanaTorneo6 = tk.Toplevel(ventanaMain)
    ventanaTorneo6.title("Torneo")
    anchoVentana = 850
    altoVentana = 450
    x = (ventanaTorneo6.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo6.winfo_screenheight() - altoVentana)//2
    ventanaTorneo6.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo6.focus_force()
    ventanaTorneo6.grab_set()
    ventanaTorneo6.resizable(False, False)
    ventanaTorneo6.configure(bg="lightgray")
    ventanaTorneo6.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaTorneo6.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo6.destroy(), sys.exit(0),))

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo6, text=f"{datosTorneo[0]}", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaTorneo6, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 15, rowheight=30)
    tabla = ttk.Treeview(frame, columns=("#", "Nombre y Apellido", "Genero", "Facultad", "Puntos", "Desempates", "Elo(+/-)", "Victorias(+)", "Medallas(+)"),show="headings")
    tabla.grid(row=0, column=0, columnspan=9, padx=5, pady=10, sticky="ew")

    tabla.column("#", anchor=tk.CENTER, width=30)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=180)
    tabla.column("Genero", anchor=tk.CENTER, width=60)
    tabla.column("Facultad", anchor=tk.CENTER, width=95)
    tabla.column("Puntos", anchor=tk.CENTER, width=60)
    tabla.column("Desempates", anchor=tk.CENTER, width=100)
    tabla.column("Elo(+/-)", anchor=tk.CENTER, width=85)
    tabla.column("Victorias(+)", anchor=tk.CENTER, width=95)
    tabla.column("Medallas(+)", anchor=tk.CENTER, width=90)

    tabla.heading("#", text="#")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Genero", text="Genero")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Puntos", text="Puntos")
    tabla.heading("Desempates", text="Desempates")
    tabla.heading("Elo(+/-)", text="Elo(+/-)")
    tabla.heading("Victorias(+)", text="Victorias(+)")
    tabla.heading("Medallas(+)", text="Medallas(+)")

    botonTerminarTorneo = tk.Button(ventanaTorneo6, text="Terminar", font=15, command=lambda:(ventanaTorneo6.destroy(), ventanaMain.deiconify(), guardarTorneo()))
    botonTerminarTorneo.pack(padx=10, pady=10, side=tk.RIGHT)

    botonVerDatos = tk.Button(ventanaTorneo6, text="Datos", font=15, command=verDatos)
    botonVerDatos.pack(padx=10, pady=10, side=tk.RIGHT)


    actualizarTabla()

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
    #interfazTorneo5()

#5to poder
#El nombre de la rosa
#Farenheit 451 1966/2018

