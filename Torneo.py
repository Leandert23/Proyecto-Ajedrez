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
            messagebox.showwarning("Advertencia", f" !El nombre solo debe tener caracteres alfanúmericos! \n Máximo 20 caracteres")
            return
        
        fecha = str(entryFecha.get_date()).replace("-", "/")

        if vl.validarEntero(spinboxParticipantes.get()) and int(spinboxParticipantes.get()) > 0:
            participantes = spinboxParticipantes.get()
        else:
            messagebox.showwarning("Advertencia", f"!La cantidad de participantes debe ser un número entero positivo de máximo 2 dígitos!")
            return

        if vl.validarEntero(spinboxRondas.get()) and int(spinboxRondas.get()) > 0:
            rondas = spinboxRondas.get()
        else:
            messagebox.showwarning("Advertencia", f"!La cantidad de rondas debe ser un número entero positivo de máximo de 2 dígitos!")
            return    

        if checkValor.get() == 1:
            invitados = "True"
        else:
            invitados = "False"

        if vl.validarTexto(entryDescripcion.get()):
            descripcion = entryDescripcion.get()
        else:
            messagebox.showwarning("Advertencia", "!La descripción no debe exceder los 15 caracteres!")
            return
        
        respuesta = bd.crearTablaAntesTorneo(nombre, fecha, participantes, rondas, invitados, descripcion)
        if respuesta == True:
            messagebox.showerror("Error", " !Ya existe un torneo con ese nombre! \n Por favor cree uno nuevo")
            return

        datosTorneo = (nombre, fecha, participantes, rondas, invitados, descripcion)
        bd.agregarDatosListaTorneos(datosTorneo[0], datosTorneo[1], datosTorneo[2], datosTorneo[3], datosTorneo[4], (f"{"Ninguna" if datosTorneo[5] == "" else datosTorneo[5]}"), "✖")
        ventanaTorneo1.destroy()
        interfazTorneo2(ventanaMain, respuesta, datosTorneo)

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
    ventanaTorneo1.title("ChessPyter")
    ventanaTorneo1.geometry(f"{ventanaMain.winfo_screenwidth()}x{ventanaMain.winfo_screenheight()-50}+{-8}+{-2}")
    ventanaTorneo1.focus_force()
    ventanaTorneo1.grab_set()
    ventanaTorneo1.resizable(False, False)
    ventanaTorneo1.configure(bg="lightgray")
    ventanaTorneo1.bind("<Escape>", lambda e:(ventanaTorneo1.destroy(), ventanaMain.deiconify()))
    ventanaTorneo1.bind("<Return>", lambda e: crearTorneo())
    ventanaTorneo1.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo1.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo1, text="  Crear Torneo  ", font=("Impact", 25))
    labelTitulo.pack(pady= (30,15))

    frame = tk.Frame(ventanaTorneo1, bd=10, bg="gray", width=500, height=500)
    frame.pack()

    labelNombre = tk.Label(frame, text="  Nombre  ", font=("Impact", 17))
    labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    labelFecha = tk.Label(frame, text="  Fecha  ", font=("Impact", 17))
    labelFecha.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelParticipantes = tk.Label(frame, text="  Participantes  ", font=("Impact", 17))
    labelParticipantes.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelRondas = tk.Label(frame, text="  Rondas  ", font=("Impact", 17))
    labelRondas.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelInvitados = tk.Label(frame, text="  Invitados  ", font=("Impact", 17))
    labelInvitados.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    labelDescripcion = tk.Label(frame, text="  Descripción  ", font=("Impact", 17))
    labelDescripcion.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    entryNombre = tk.Entry(frame, font=("Impact", 16))
    entryNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    ventanaTorneo1.after(10, lambda:entryNombre.focus())

    entryFecha = DateEntry(frame, date_pattern='dd/mm/yy', font=("Impact", 16), state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    spinboxParticipantes = tk.Spinbox(frame, from_=1, to=10, font=("Impact", 16))
    spinboxParticipantes.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxRondas = tk.Spinbox(frame, from_=1, to=10, font=("Impact", 16))
    spinboxRondas.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    checkValor = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValor, onvalue=1, offvalue=0)
    checkInvitados.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame, font=("Impact", 16))
    entryDescripcion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="  Limpiar  ", font=("Impact", 17), command=limpiar)
    botonLimpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    botonCrear = tk.Button(frame, text="  Crear  ", font=("Impact", 17),  command=crearTorneo)
    botonCrear.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

def interfazTorneo2(ventanaMain, nombreTorneo, datosTorneo):
    #Funciones
    def actualizarTabla():
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosAntesTorneo(nombreTorneo)

        if datos == None:
            ventanaTorneo2.destroy()
            ventanaMain.deiconify()
            messagebox.showerror("Error", f" !!Error al cargar torneo!! \n Torneo {nombreTorneo} no encontrado")
            return

        if len(datos) > 0:
            labelJugadoresInscritos.config(text=f"  Jugadores inscritos: {len(datos)}/{datosTorneo[2]}  ")
        else:
            labelJugadoresInscritos.config(text=f"  Jugadores inscritos: 0/{datosTorneo[2]}  ")
            return
        
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
        interfazTorneo4(ventanaTorneo2, actualizarTabla, nombreTorneo, datos[0], datos[4], datos[5], datos[6], datos[8], datosTorneo)

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

        respuesta = messagebox.askyesno("Cargar Torneo", "¿Estás seguro de cargar el torneo? \n !Una vez cargado no se podrán editar los atributos del torneo!")
        if respuesta:
            if len(jugadoresInscritos) != int(datosTorneo[2]):
                messagebox.showerror("Error", f" !!Debe haber {datosTorneo[2]} jugador/es inscritos para cargar el torneo!!")
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
                respuesta2 = bd.consultarDatosJugador(respuesta, jugadores[0], desempatesJugadores[i])
                i += 1
                if respuesta2:
                    ventanaTorneo2.destroy()
                    ventanaMain.deiconify()
                    messagebox.showerror("Error", f" !!Error al cargar torneo!! \n Torneo {nombreTorneo} no encontrado")
                    bd.eliminarTabla("AT_"+nombreTorneo[3:])
                    bd.eliminarTabla("DT_"+nombreTorneo[3:])
                    return
            
            ventanaTorneo2.destroy()
            interfazTorneo6(ventanaMain, respuesta, datosTorneo, estadisticasJugadores)

    def eliminarTorneo():
        respuesta = messagebox.askyesno("Salir", f" Si sale en este momento el torneo será eliminado \n ¿Guardar Torneo?")
        if respuesta == False:
            bd.eliminarTorneo(datosTorneo[0], nombreTorneo[3:])

        ventanaTorneo2.destroy()
        ventanaMain.deiconify()

    #Ventana
    ventanaTorneo2 = tk.Toplevel(ventanaMain)
    ventanaTorneo2.title("ChessPyter")
    ventanaTorneo2.geometry(f"{ventanaTorneo2.winfo_screenwidth()}x{ventanaTorneo2.winfo_screenheight()-50}+{-8}+{-2}")
    ventanaTorneo2.focus_force()
    ventanaTorneo2.grab_set()
    ventanaTorneo2.resizable(False, False)
    ventanaTorneo2.configure(bg="lightgray")
    ventanaTorneo2.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaTorneo2.bind("<Escape>", lambda e: eliminarTorneo())
    ventanaTorneo2.bind("<Return>", lambda e: cargarTorneo())
    ventanaTorneo2.protocol("WM_DELETE_WINDOW", eliminarTorneo)
    ventanaTorneo2.deiconify()

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo2, text=f"  {datosTorneo[0]}  ", font=("Impact", 25))
    labelTitulo.pack(pady= (30,15))

    frame = tk.Frame(ventanaTorneo2, bd=10, bg="gray", width=500, height=500)
    frame.pack()
    frame.grid_columnconfigure(3, minsize=100, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=("Impact", 17))
    estilo.configure("Treeview", rowheight= 35, font=("Impact", 16))
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido", "Género", "Facultad", "Elo", "Victorias", "Tablas", "Derrotas", "Puntos", "Desempates", "Diferencia Elo"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=9, padx=5, pady=10, sticky="ew") 
    tabla.bind("<Button-3>", menu)

    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Género", anchor=tk.CENTER, width=120)
    tabla.column("Facultad", anchor=tk.CENTER, width=145)
    tabla.column("Elo", anchor=tk.CENTER, width=95)
    tabla.column("Victorias", anchor=tk.CENTER, width=125)
    tabla.column("Tablas", anchor=tk.CENTER, width=125)
    tabla.column("Derrotas", anchor=tk.CENTER, width=125)
    tabla.column("Puntos", anchor=tk.CENTER, width=110)
    tabla.column("Desempates", anchor=tk.CENTER, width=160)
    tabla.column("Diferencia Elo", anchor=tk.CENTER, width=0, stretch=False, minwidth=0)
    
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Género", text="Género")
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

    labelJugadoresInscritos = tk.Label(frame, text=f"  Jugadores inscritos: 0/{datosTorneo[2]}  ", bg="lightgray", font=("Impact", 16))
    labelJugadoresInscritos.grid(row=1, column=0, pady=5, sticky="e")
    
    labelRondas = tk.Label(frame, text=f"  Rondas: {datosTorneo[3]} ", bg="lightgray", font=("Impact", 16))
    labelRondas.grid(row=1, column=1, pady=5, sticky="ew")

    labelInvitados = tk.Label(frame, text=f"  Invitados: {"Si" if datosTorneo[4] == "True" else "No"}  ", bg="lightgray", font=("Impact", 16))
    labelInvitados.grid(row=1, column=2, pady=5, sticky="w")

    botonAgregarJugador = tk.Button(frame, text="  Agregar  ", font=("Impact", 14), bg="lightgray", command=lambda:(interfazTorneo3(ventanaTorneo2, nombreTorneo, actualizarTabla)))
    botonAgregarJugador.grid(row=1, column=4, pady=5, padx=5, sticky="e")

    botonEditarTorneo = tk.Button(frame, text="  Editar  ", font=("Impact", 14), bg="lightgray", command= lambda:(interfazTorneo5(ventanaMain, ventanaTorneo2, nombreTorneo, datosTorneo)))
    botonEditarTorneo.grid(row=1, column=5, pady=5, padx=5, sticky="ew")

    botonCargarTorneo = tk.Button(frame, text="  Cargar  ", font=("Impact", 14), bg="lightgray", command= cargarTorneo)
    botonCargarTorneo.grid(row=1, column=6, pady=5, padx=5, sticky="w")

    actualizarTabla()

def interfazTorneo3(ventana, nombreTorneo, funcion):
    #Funciones
    def filtrarJugadores():
        datos = bd.consultarDatosJugadores("Nombre")
        
        if datos == True:
            ventana.attributes('-disabled', False)
            messagebox.showerror("Error", " !!Error al consultar!! \n Jugadores no encontrados")
            return
        
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
            messagebox.showerror("Error", " !!Este jugador ya está inscrito!! \n Por favor ingrese uno diferente")
            return
        elif respuesta == False:
            messagebox.showerror("Error", " !!Error al agregar Jugador!! \n Tabla jugadores no encontrada")
            return
    
        ventana.attributes('-disabled', False)
        ventanaTorneo3.destroy()
        funcion()

    def eliminarTorneo():
        respuesta = messagebox.askyesno("Salir", f" Si sale en este momento el torneo será eliminado \n ¿Seguro de salir?")
        if respuesta:
            ventanaTorneo3.destroy()
            bd.eliminarTabla(nombreTorneo)
            sys.exit(0)

    #Ventana
    ventanaTorneo3 = tk.Toplevel(ventana)
    ventanaTorneo3.title("ChessPyter")
    anchoVentana = 325
    altoVentana = 475
    x = (ventanaTorneo3.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo3.winfo_screenheight() - altoVentana)//2
    ventanaTorneo3.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo3.focus_force()
    ventanaTorneo3.grab_set()
    ventanaTorneo3.resizable(False, False)
    ventanaTorneo3.configure(bg="lightgray")
    ventanaTorneo3.bind("<Escape>", lambda e:(ventana.attributes('-disabled', False), ventanaTorneo3.destroy()))
    ventanaTorneo3.protocol("WM_DELETE_WINDOW", eliminarTorneo)
    ventana.attributes('-disabled', True)

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo3, text=f"  Agregar Jugador  ", font=("Impact", 20))
    labelTitulo.pack(pady=(20, 10)) 

    frame = tk.Frame(ventanaTorneo3, bd=10, bg="gray", width=500, height=500)
    frame.pack()  
        
    listaJugadores = tk.Listbox(frame, width=20, height=10, font=("Impact", 17))
    listaJugadores.grid(row=0, column=0, sticky="ew")
    listaJugadores.bind("<Double-Button-1>", lambda e:seleccionarJugador())

    entryBusqueda = tk.Entry(frame, font=("Impact", 16))
    entryBusqueda.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
    ventanaTorneo3.after(100, lambda:entryBusqueda.focus())
    entryBusqueda.bind("<KeyRelease>", lambda e:filtrarJugadores())

    filtrarJugadores()

def interfazTorneo4(ventana, funcion, nombreTorneo, nombreJugador, vict, tabl, derro, desemp, datosTorneo):
    #Funciones
    def insertarDatos():
        spinboxVictorias.delete(0, tk.END)
        spinboxTablas.delete(0, tk.END)
        spinboxDerrotas.delete(0, tk.END)
        spinboxDesempate1.delete(0, tk.END)
        spinboxDesempate2.delete(0, tk.END)
        desempates = desemp.split("  ")
        spinboxVictorias.insert(0,f"{vict[2:-1] if vict != "0" else "0"}")
        spinboxTablas.insert(0, f"{tabl[2:-1] if tabl != "0" else "0"}")
        spinboxDerrotas.insert(0, f"{derro[2:-1] if derro != "0" else "0"}")
        spinboxDesempate1.insert(0, desempates[0])
        spinboxDesempate2.insert(0, desempates[1])

    def editarJugador():
        eloVictorias = vl.validarEloVictorias(spinboxVictorias.get())
        numeroVictorias = len(spinboxVictorias.get())
        if eloVictorias == "False":
            messagebox.showwarning("Advertencia", f" !Símbolo incorrecto (Victorias)! \n Permitidos ( + - = )")
            return
        
        if spinboxVictorias.get() == "0":
            numeroVictorias = 0
        
        eloTablas = vl.validarEloTablas(spinboxTablas.get())
        numeroTablas = len(spinboxTablas.get())
        if eloTablas == "False":
            messagebox.showwarning("Advertencia", f" !Símbolo incorrecto (Tablas)! \n Permitidos ( + - )")
            return
        
        if spinboxTablas.get() == "0":
            numeroTablas = 0
        
        eloDerrotas = vl.validarEloDerrotas(spinboxDerrotas.get())
        numeroDerrotas = len(spinboxDerrotas.get())
        if eloDerrotas == "False":
            messagebox.showwarning("Advertencia", f" !Símbolo incorrecto (Derrotas)! \n Permitidos ( + - = )")
            return
        
        if spinboxDerrotas.get() == "0":
            numeroDerrotas = 0
        
        if vl.validarFloat(spinboxDesempate1.get()):
            desempate1 = spinboxDesempate1.get()
        else:
            messagebox.showwarning("Advertencia", f"!El desempate(1) debe ser un número decimal positivo!")
            return
        
        if vl.validarFloat((spinboxDesempate2.get())):
            desempate2 = spinboxDesempate2.get()
        else:
            messagebox.showwarning("Advertencia", f"!El desempate(2) debe ser un número decimal positivo!")
            return

        estadisticas = numeroVictorias + numeroTablas + numeroDerrotas
        diferenciaElo = eloVictorias + eloTablas + eloDerrotas
        if estadisticas != int(datosTorneo[3]):
            messagebox.showwarning("Advertencia", f"!La cantidad de ( victorias + tablas + derrotas ) debe ser igual al numero de rondas: ( {datosTorneo[3]} )!")
            return

        if numeroVictorias == 0:
            victorias = "0"
        else:
            victorias = f"{numeroVictorias}({spinboxVictorias.get()})"

        if numeroTablas == 0:
            tablas = "0"
        else:
            tablas = f"{numeroTablas}({spinboxTablas.get()})"
        
        if numeroDerrotas == 0:
            derrotas= "0"
        else:
            derrotas = f"{numeroDerrotas}({spinboxDerrotas.get()})"

        puntos = int(numeroVictorias) + int(numeroTablas)/2
        bd.actualizarJugadorTorneo(nombreTorneo, nombreJugador, victorias, tablas, derrotas, puntos, round(float(desempate1),2), round(float(desempate2),2), diferenciaElo)
        ventana.attributes('-disabled', False)
        ventanaTorneo4.destroy()
        funcion()

    def limpiar():
        spinboxVictorias.delete(0, tk.END)
        spinboxTablas.delete(0, tk.END)
        spinboxDerrotas.delete(0, tk.END)
        spinboxDesempate1.delete(0, tk.END)
        spinboxDesempate2.delete(0, tk.END) 
        spinboxVictorias.focus()

    #Ventana
    ventanaTorneo4 = tk.Toplevel(ventana)
    ventanaTorneo4.title("ChessPyter")
    anchoVentana = 475
    altoVentana = 475
    x = (ventanaTorneo4.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo4.winfo_screenheight() - altoVentana)//2
    ventanaTorneo4.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo4.resizable(False, False)
    ventanaTorneo4.focus_force()
    ventanaTorneo4.grab_set()
    ventanaTorneo4.configure(bg="lightgray")
    ventanaTorneo4.bind("<Escape>", lambda e:(ventana.attributes('-disabled', False), ventanaTorneo4.destroy()))
    ventanaTorneo4.bind("<Return>", lambda e: editarJugador())
    ventanaTorneo4.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo4.destroy(), sys.exit(0)))
    ventana.attributes('-disabled', True)

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo4, text="  Editar Jugador  ", font=("Impact", 20))
    labelTitulo.pack(pady= (20,10))

    frame = tk.Frame(ventanaTorneo4, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelVictorias = tk.Label(frame, text="  Victorias  ", font=("Impact", 17))
    labelVictorias.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelTablas = tk.Label(frame, text="  Tablas  ", font=("Impact", 17))
    labelTablas.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelDerrotas = tk.Label(frame, text="  Derrotas  ", font=("Impact", 17))
    labelDerrotas.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelDesempate1 = tk.Label(frame, text="  Desempate1  ", font=("Impact", 17))
    labelDesempate1.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelDesempate2 = tk.Label(frame, text="  Desempate2  ", font=("Impact", 17))
    labelDesempate2.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    spinboxVictorias = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxVictorias.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    ventanaTorneo4.after(10, lambda:spinboxVictorias.focus())

    spinboxTablas = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxTablas.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    spinboxDerrotas = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxDerrotas.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxDesempate1 = tk.Spinbox(frame, from_=0.00, to=99.00, increment=0.5, format="%.2f", font=("Impact", 16))
    spinboxDesempate1.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    spinboxDesempate2 = tk.Spinbox(frame, from_=0.00, to=99.00, increment=0.5, format="%.2f", font=("Impact", 16))
    spinboxDesempate2.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="  Limpiar  ", font=("Impact", 17), command=limpiar)
    botonLimpiar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="  Editar  ", font=("Impact", 17), command=editarJugador)
    botonEditar.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    insertarDatos()

def interfazTorneo5(ventanaMain, ventana, nombreTorneo, datosTorneo):
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
            messagebox.showwarning("Advertencia", f" !El nombre solo debe tener caracteres alfanúmericos! \n Máximo 20 caracteres")
            return
        
        fecha = str(entryFecha.get_date()).replace("-", "/")

        if vl.validarEntero(spinboxParticipantes.get()):
            participantes = spinboxParticipantes.get()
        else:
            messagebox.showwarning("Advertencia", f"!La cantidad de participantes debe ser un número entero positivo de máximo 2 dígitos!")
            return

        if vl.validarEntero(spinboxRondas.get()):
            rondas = spinboxRondas.get()
        else:
            messagebox.showwarning("Advertencia", f"!La cantidad de rondas debe ser un número entero positivo de máximo 2 dígitos!")
            return    

        if checkValor.get() == 1:
            invitados = "True"
        else:
            invitados = "False"

        if vl.validarTexto(entryDescripcion.get()):
            descripcion = entryDescripcion.get()
        else:
            messagebox.showwarning("Advertencia", "!La descripción no debe exceder los 15 caracteres!")
            return
        
        respuesta = bd.editarTablaAntesTorneo(nombreTorneo, nombre, fecha, participantes, rondas, invitados, descripcion)
        if respuesta == True:
            messagebox.showerror("Error", " !!Ya existe un torneo con estos datos!! \n Por favor ingrese uno nuevo")
            return
        
        ventana.attributes('-disabled', False)
        ventana.destroy()
        datosTorneo = (nombre, fecha, participantes, rondas, invitados, descripcion)
        ventanaTorneo5.destroy()
        interfazTorneo2(ventanaMain, respuesta, datosTorneo)

    def eliminarTorneo():
        respuesta = messagebox.askyesno("Salir", f" Si sale en este momento el torneo será eliminado \n ¿Seguro de salir?")
        if respuesta:
            ventanaTorneo5.destroy()
            bd.eliminarTabla(nombreTorneo)
            sys.exit(0)

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
    ventanaTorneo5.title("ChessPyter")
    anchoVentana = 500
    altoVentana = 525
    x = (ventanaTorneo5.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo5.winfo_screenheight() - altoVentana)//2
    ventanaTorneo5.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaTorneo5.grab_set()
    ventanaTorneo5.focus_force()
    ventanaTorneo5.resizable(False, False)
    ventanaTorneo5.configure(bg="lightgray")
    ventanaTorneo5.bind("<Escape>", lambda e:(ventana.attributes('-disabled', False), ventanaTorneo5.destroy()))
    ventanaTorneo5.protocol("WM_DELETE_WINDOW", eliminarTorneo)
    ventanaTorneo5.bind("<Return>", lambda e: editarTorneo())
    ventana.attributes('-disabled', True)

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo5, text="  Editar Torneo  ", font=("Impact", 20))
    labelTitulo.pack(pady= (20, 10))

    frame = tk.Frame(ventanaTorneo5, bd=10, bg="gray", width=500, height=500)
    frame.pack()

    labelNombre = tk.Label(frame, text="  Nombre  ", font=("Impact", 17))
    labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelFecha = tk.Label(frame, text="  Fecha  ", font=("Impact", 17))
    labelFecha.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelParticipantes = tk.Label(frame, text="  Participantes  ", font=("Impact", 17))
    labelParticipantes.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelRondas = tk.Label(frame, text="  Rondas  ", font=("Impact", 17))
    labelRondas.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelInvitados = tk.Label(frame, text="  Invitados  ", font=("Impact", 17))
    labelInvitados.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    labelDescripcion = tk.Label(frame, text="  Descripción  ", font=("Impact", 17))
    labelDescripcion.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    entryNombre = tk.Entry(frame, font=("Impact", 16))
    entryNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    ventanaTorneo5.after(10, lambda:entryNombre.focus())

    entryFecha = DateEntry(frame, date_pattern='dd/mm/yy', bg="gray", font=("Impact", 16), state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    spinboxParticipantes = tk.Spinbox(frame, from_=1, to=100, font=("Impact", 16))
    spinboxParticipantes.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxRondas = tk.Spinbox(frame, from_=1, to=100, font=("Impact", 16))
    spinboxRondas.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    checkValor = tk.IntVar()
    checkInvitados = tk.Checkbutton(frame, variable=checkValor, onvalue=1, offvalue=0)
    checkInvitados.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame, font=("Impact", 16))
    entryDescripcion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="  Limpiar  ", font=("Impact", 17), command=limpiar)
    botonLimpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="  Editar  ", font=("Impact", 17),  command=editarTorneo)
    botonEditar.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

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
        if datos == None:
            ventanaTorneo6.destroy()
            ventanaMain.deiconify()
            messagebox.showerror("Error", f" !!Error al cargar torneo!! \n Torneo {nombreTorneo} no encontrado!!")
            print("AT_"+nombreTorneo[3:])
            bd.eliminarTabla("AT_"+nombreTorneo[3:])
            bd.eliminarTabla("DT_"+nombreTorneo[3:])
            return
        
        posiciones = 0
        femenino = True
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
            tabla.tag_configure("Oro", background="#DEDE2C", foreground="#FFFFFF", font=("Impact", 16, "italic"))
            tabla.tag_configure("Plata", background="#545050", foreground="#FFFFFF", font=("Impact", 16, "italic"))
            tabla.tag_configure("Bronce", background="#8D4416", foreground="#FFFFFF", font=("Impact", 16, "italic"))
            tabla.tag_configure("Femenina", background="#DE2C50", foreground="#FFFFFF", font=("Impact", 16, "italic"))
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
                                                        #       [Nombre y Apellido], Genero, Facultad,        Puntos,                Desempates,                                                                                              Elo,                                                                                                          Victorias,                                                         Medallas,                Torneos,
            if posiciones <= 2:
                if posiciones == 0:
                    tag = "Oro"
                elif posiciones == 1:
                    tag = "Plata"
                else:
                    tag = "Bronce"
                tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}{f'(+{estadisticasJugadores[indice][1]})' if int(estadisticasJugadores[indice][1]) > 0 else "" }"), (f"{registro[5]}(+1)")), tags=(tag))
                bd.actualizarDatosJugador(registro[0], registro[2], (int(registro[3])+(int(estadisticasJugadores[indice][2])+participantes)), (int(registro[4])+int(estadisticasJugadores[indice][1])), (int(registro[6])+1), (int(registro[5])+1), tag)
                bd.actualizarTablaDespuesTorneo(nombreTorneo, registro[0], (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}{f'(+{estadisticasJugadores[indice][1]})' if int(estadisticasJugadores[indice][1]) > 0 else "" }"), (f"{registro[5]}(+1)"))
                posiciones += 1
                participantes -= 1
            elif femenino == True and registro[1] == "F":
                tag = "Femenina"
                tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"),(f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}{f'(+{estadisticasJugadores[indice][1]})' if int(estadisticasJugadores[indice][1]) > 0 else "" }"), (f"{registro[5]}(+1)")), tags=(tag))
                bd.actualizarDatosJugador(registro[0], registro[2], (int(registro[3])+(int(estadisticasJugadores[indice][2])+participantes)), (int(registro[4])+int(estadisticasJugadores[indice][1])), (int(registro[6])+1), (int(registro[5])+1), "Otra")
                bd.actualizarTablaDespuesTorneo(nombreTorneo, registro[0], (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}{f'(+{estadisticasJugadores[indice][1]})' if int(estadisticasJugadores[indice][1]) > 0 else "" }"), (f"{registro[5]}(+1)"))
                posiciones += 1
                participantes -= 1
                femenino = False
            else:
                tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}{f'(+{estadisticasJugadores[indice][1]})' if int(estadisticasJugadores[indice][1]) > 0 else "" }"), registro[5]), tags=(tag))
                bd.actualizarDatosJugador(registro[0], registro[2], (int(registro[3])+(int(estadisticasJugadores[indice][2])+participantes)), (int(registro[4])+int(estadisticasJugadores[indice][1])), (int(registro[6])+1), int(registro[5]))
                bd.actualizarTablaDespuesTorneo(nombreTorneo, registro[0], (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}{f'(+{estadisticasJugadores[indice][1]})' if int(estadisticasJugadores[indice][1]) > 0 else "" }"), registro[5])
                posiciones += 1
                participantes -= 1
            #tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], (f"{registro[3] + estadisticasJugadores[0]}"), (f"{registro[4] + estadisticasJugadores[1]}"),(f"{registro[5] + estadisticasJugadores[1]}")), tags=(tag))
                                            #"#", "Nombre y Apellido", "Genero", "Facultad", "Elo(+/-)", "Victorias(+)", "Medallas(+)"   
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=10, sticky="ns")

    bd.actualizarTablaListaTorneo(datosTorneo[0])

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    def verDatos():
        messagebox.showinfo("Información Torneo", f" Nombre: {datosTorneo[0]} \n Fecha: {datosTorneo[1]} \n Participantes: {datosTorneo[2]} \n Rondas: {datosTorneo[3]} \n Invitados: {"Si" if datosTorneo[4] == "True" else "No"} \n Descripción: {"Ninguna" if datosTorneo[5] == "" else datosTorneo[5]}")

    ventanaTorneo6 = tk.Toplevel(ventanaMain)
    ventanaTorneo6.title("ChessPyter")
    ventanaTorneo6.geometry(f"{ventanaTorneo6.winfo_screenwidth()}x{ventanaTorneo6.winfo_screenheight()-50}+{-8}+{-2}")
    ventanaTorneo6.focus_force()
    ventanaTorneo6.grab_set()
    ventanaTorneo6.resizable(False, False)
    ventanaTorneo6.configure(bg="lightgray")
    ventanaTorneo6.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaTorneo6.protocol("WM_DELETE_WINDOW", lambda: (ventanaTorneo6.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaTorneo6, text=f"  {datosTorneo[0]}  ", font=("Impact", 25))
    labelTitulo.pack(pady= (30,15))

    frame = tk.Frame(ventanaTorneo6, bd=10, bg="gray", width=500, height=500)
    frame.pack()
    frame.grid_columnconfigure(0, minsize=100, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=("Impact", 17))
    estilo.configure("Treeview", rowheight= 35, font=("Impact", 16))
    tabla = ttk.Treeview(frame, columns=("#", "Nombre y Apellido", "Género", "Facultad", "Puntos", "Desempates", "Elo(+/-)", "Victorias(+)", "Medallas(+)"),show="headings")
    tabla.grid(row=0, column=0, columnspan=9, padx=5, pady=10, sticky="ew")

    tabla.column("#", anchor=tk.CENTER, width=60)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Género", anchor=tk.CENTER, width=120)
    tabla.column("Facultad", anchor=tk.CENTER, width=145)
    tabla.column("Puntos", anchor=tk.CENTER, width=110)
    tabla.column("Desempates", anchor=tk.CENTER, width=140)
    tabla.column("Elo(+/-)", anchor=tk.CENTER, width=125)
    tabla.column("Victorias(+)", anchor=tk.CENTER, width=145)
    tabla.column("Medallas(+)", anchor=tk.CENTER, width=150)

    tabla.heading("#", text="#")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Género", text="Género")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Puntos", text="Puntos")
    tabla.heading("Desempates", text="Desempates")
    tabla.heading("Elo(+/-)", text="Elo(+/-)")
    tabla.heading("Victorias(+)", text="Victorias(+)")
    tabla.heading("Medallas(+)", text="Medallas(+)")

    botonVerDatos = tk.Button(frame, text="  Datos  ", font=("Impact", 16), command=verDatos)
    botonVerDatos.grid(row=1, column=0, pady=5, padx=5, sticky="e")

    botonTerminarTorneo = tk.Button(frame, text="  Terminar  ", font=("Impact", 16), command=lambda:(ventanaTorneo6.destroy(), ventanaMain.deiconify()))
    botonTerminarTorneo.grid(row=1, column=1, pady=5, padx=5, sticky="w")

    actualizarTabla()

def editarTorneo():
    pass

def borrarTorneo():
    pass

def filtrarTorneos():
    pass
