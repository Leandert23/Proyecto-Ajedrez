import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkinter import ttk, messagebox
import sys

def interfazJugadores1(ventanaMain):
    #Funciones
    def cargarJugadores(filtro="Nombre"):
        for fila in tabla.get_children():
            tabla.delete(fila)

        datos = bd.consultarDatosJugadores(filtro)

        if datos == True:
            ventanaJugadores1.attributes('-disabled', False)
            messagebox.showerror("Error", " !!Error al consultar datos!! \n Jugadores no encontrados")
            return
        
        if len(datos) > 0:
            labelJugadores.config(text=f"  Jugadores: {len(datos)}  ")
        else:
            labelJugadores.config(text=f"  Jugadores: 0  ")
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
            
            tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6]), tags=(tag))
            
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    def menu(evento):
        fila = tabla.identify_row(evento.y)
        if fila:
            tabla.selection_set(fila)
            menu.tk_popup(evento.x_root, evento.y_root)
    
    def editarJugador():
        fila = tabla.selection()
        datos = tabla.item(fila, 'values')
        interfazJugadores3(ventanaJugadores1, cargarJugadores, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])

    def borrarJugador():
        item = tabla.selection()
        valores = tabla.item(item, 'values')
        respuesta = messagebox.askyesno("Borrar", f"¿Estás seguro de borrar a {valores[0]}?")
        if respuesta:
            bd.eliminarDatosJugador(valores[0])
            cargarJugadores()

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)

    #Ventana
    ventanaJugadores1 = tk.Toplevel(ventanaMain)
    ventanaJugadores1.title("ChessPyter")
    ventanaJugadores1.geometry(f"{ventanaJugadores1.winfo_screenwidth()}x{ventanaJugadores1.winfo_screenheight()-50}+{-8}+{-2}")
    ventanaJugadores1.focus_force()
    ventanaJugadores1.grab_set()
    ventanaJugadores1.resizable(False, False)
    ventanaJugadores1.configure(bg="lightgray")
    ventanaJugadores1.bind("<Escape>", lambda e:(ventanaMain.deiconify(), ventanaJugadores1.destroy()))
    ventanaJugadores1.bind("<Double-Button-1>", lambda e:desseleccionarFila())
    ventanaJugadores1.protocol("WM_DELETE_WINDOW", lambda: (ventanaJugadores1.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaJugadores1, text=f"  Jugadores  ", font=("Impact", 25))
    labelTitulo.pack(pady= (30,15))

    frame = tk.Frame(ventanaJugadores1, bd=10, bg="gray", width=500, height=500)
    frame.pack()
    frame.grid_columnconfigure(0, minsize=100, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font=("Impact", 17))
    estilo.configure("Treeview", rowheight= 35, font=("Impact", 16))
    tabla = ttk.Treeview(frame, columns=("Nombre y Apellido","Género", "Facultad", "Elo", "Victorias", "Torneos", "Medallas"), show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")
    tabla.bind("<Button-3>", menu)

    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Género", anchor=tk.CENTER, width=120)
    tabla.column("Facultad", anchor=tk.CENTER, width=140)
    tabla.column("Elo", anchor=tk.CENTER, width=100)
    tabla.column("Victorias", anchor=tk.CENTER, width=120)
    tabla.column("Torneos", anchor=tk.CENTER, width=120)
    tabla.column("Medallas", anchor=tk.CENTER, width=120)

    tabla.heading("Nombre y Apellido", text="Nombre y Apellido", command=lambda:cargarJugadores())
    tabla.heading("Género", text="Género", command=lambda:cargarJugadores("Genero"))
    tabla.heading("Facultad", text="Facultad", command=lambda:cargarJugadores("Facultad"))
    tabla.heading("Elo", text="Elo", command=lambda:cargarJugadores("Elo"))
    tabla.heading("Victorias", text="Victorias", command=lambda:cargarJugadores("Victorias"))
    tabla.heading("Torneos", text="Torneos", command=lambda:cargarJugadores("Torneos"))
    tabla.heading("Medallas", text="Medallas", command=lambda:cargarJugadores("Medallas"))

    menu = tk.Menu(ventanaJugadores1, tearoff=0)
    menu.add_command(label="Editar", command=editarJugador)
    menu.add_command(label="Borrar", command=borrarJugador)    
    
    labelJugadores = tk.Label(frame, text="  Jugadores: 0  ", bg="lightgray", font=("Impact", 16))
    labelJugadores.grid(row=1, column=0, sticky="w")

    labelBusqueda = tk.Label(frame, text="  Buscar:  ", bg="lightgray", font=("Impact", 16))
    labelBusqueda.grid(row=1, column=1, sticky="w")

    entryBusqueda = tk.Entry(frame, font=("Impact", 16))
    entryBusqueda.grid(row=1, column=2, padx=(0,20), sticky="ew")
    ventanaJugadores1.after(100, lambda:entryBusqueda.focus())
    entryBusqueda.bind("<KeyRelease>", lambda e:cargarJugadores(entryBusqueda.get()))

    botonCrearJugador = tk.Button(frame, text="  Agregar  ", bg="lightgray", font=("Impact", 14), command=lambda:interfazJugadores2(ventanaJugadores1, cargarJugadores))
    botonCrearJugador.grid(row=1, column=3, pady=5, padx=5, sticky="e")

    cargarJugadores()

def interfazJugadores2(ventana, funcion):
    #Funciones
    def crearJugador():
        if vl.validarNombre(entryNombreCompleto.get()) and len(entryNombreCompleto.get()) <= 20:
            nombreCompleto = entryNombreCompleto.get()
        else:
            messagebox.showwarning("Advertencia", f" !El nombre solo debe tener caracteres alfanúmericos! \n Maximo 20 caracteres")
            return
        
        genero = menuGeneros.cget("text")

        facultad = menuFacultades.cget("text")
    
        if vl.validarEntero(spinboxElo.get()) and len(vl.validarEntero2(spinboxElo.get())) == 4:
            elo = spinboxElo.get()
        else:
            messagebox.showwarning("Advertencia", f"!El elo debe ser un numero entero positivo de 4 dígitos!")
            return
        
        if vl.validarEntero(spinboxVictorias.get()) and len(vl.validarEntero2(spinboxVictorias.get())) <= 2:
            victorias = spinboxVictorias.get()
        else:
            messagebox.showwarning("Advertencia", f"!El número de victorias debe ser un numero entero positivo de máximo 2 dígitos!")
            return
        
        if vl.validarEntero(spinboxTorneos.get()) and len(vl.validarEntero2(spinboxTorneos.get())) <= 2:
            torneos = spinboxTorneos.get()
        else:
            messagebox.showwarning("Advertencia", f"!El número de torneos debe ser un numero entero positivo de máximo 2 dígitos!")
            return
        
        if vl.validarEntero(spinboxMedallas.get()) and len(vl.validarEntero2(spinboxMedallas.get())) <= 2:
            if int(spinboxMedallas.get()) <= int(spinboxTorneos.get()):
                medallas = spinboxMedallas.get()
            else:
                messagebox.showwarning("Advertencia", f"!El número de medallas debe ser menor o igual al número de torneos!")
                return
        else:
            messagebox.showwarning("Advertencia", f"!El número de medallas debe ser un numero entero positivo de máximo 2 dígitos!")
            return

        respuesta = bd.agregarDatosJugadores(nombreCompleto, genero[0], facultad, elo, victorias, torneos, medallas)
        if respuesta == True:
            messagebox.showwarning("Advertencia", f" !El jugador {nombreCompleto} ya está agregado \n Por favor agregue uno nuevo")
            return
        
        ventana.attributes('-disabled', False) 
        ventanaJugadores2.destroy()
        funcion()
    
    def nuevoJugador():
        if checkValorNuevo.get() == 1:
            spinboxElo.delete(0, tk.END)
            spinboxVictorias.delete(0, tk.END)
            spinboxTorneos.delete(0, tk.END)
            spinboxMedallas.delete(0, tk.END) 
            spinboxElo.insert(0, "1500")
            spinboxElo.config(state=tk.DISABLED)
            spinboxVictorias.insert(0, "0")
            spinboxVictorias.config(state=tk.DISABLED)
            spinboxMedallas.insert(0, "0")
            spinboxMedallas.config(state=tk.DISABLED)
            spinboxTorneos.insert(0, "0")
            spinboxTorneos.config(state=tk.DISABLED)
            spinboxMedallas.insert(0, "0")
            spinboxMedallas.config(state=tk.DISABLED)
            return
        
        spinboxElo.config(state=tk.NORMAL)
        spinboxElo.delete(0, tk.END)
        spinboxVictorias.config(state=tk.NORMAL)
        spinboxVictorias.delete(0, tk.END)
        spinboxMedallas.config(state=tk.NORMAL)
        spinboxMedallas.delete(0, tk.END)
        spinboxTorneos.config(state=tk.NORMAL)
        spinboxTorneos.delete(0, tk.END)
        spinboxMedallas.config(state=tk.NORMAL)
        spinboxMedallas.delete(0, tk.END) 

    def limpiar():
        checkValorNuevo.set(0)
        entryNombreCompleto.delete(0, tk.END)
        menuGeneros.config(text="Masculino")
        menuFacultades.config(text="Ingeniería")
        spinboxElo.config(state=tk.NORMAL)
        spinboxElo.delete(0, tk.END)
        spinboxVictorias.config(state=tk.NORMAL)
        spinboxVictorias.delete(0, tk.END)
        spinboxTorneos.config(state=tk.NORMAL)
        spinboxTorneos.delete(0, tk.END)
        spinboxMedallas.config(state=tk.NORMAL)
        spinboxMedallas.delete(0, tk.END) 
        entryNombreCompleto.focus()

    #Ventana
    ventanaJugadores2 = tk.Toplevel(ventana)
    ventanaJugadores2.title("ChessPyter")
    anchoVentana = 550
    altoVentana = 600
    x = (ventanaJugadores2.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaJugadores2.winfo_screenheight() - altoVentana)//2
    ventanaJugadores2.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y-50}")
    ventanaJugadores2.resizable(False, False)
    ventanaJugadores2.focus_force()
    ventanaJugadores2.grab_set()
    ventanaJugadores2.configure(bg="lightgray")
    ventanaJugadores2.bind("<Escape>", lambda e:(ventana.attributes('-disabled', False), ventanaJugadores2.destroy()))
    ventanaJugadores2.bind("<Return>", lambda e: crearJugador())
    ventanaJugadores2.protocol("WM_DELETE_WINDOW", lambda: (ventanaJugadores2.destroy(), sys.exit(0)))
    ventana.attributes('-disabled', True)

    #Widgets
    labelTitulo = tk.Label(ventanaJugadores2, text="  Agregar Jugador  ", font=("Impact", 20))
    labelTitulo.pack(pady= (20, 10))

    frame = tk.Frame(ventanaJugadores2, bd=10, bg="gray", width=500, height=500)
    frame.pack()

    checkValorNuevo = tk.IntVar()
    checkJugadorNuevo= tk.Checkbutton(frame, text="  Jugador Nuevo  ", variable=checkValorNuevo, font=("Impact", 14), onvalue=1, offvalue=0, command=nuevoJugador)
    checkJugadorNuevo.grid(row=0, column=0, columnspan=2, padx=10, pady=8, sticky="ew")

    labelNombreCompleto = tk.Label(frame, text="  Nombre y Apellido  ", font=("Impact", 17))
    labelNombreCompleto.grid(row=1, column=0, padx=10, pady=8, sticky="ew")

    labelGenero = tk.Label(frame, text="  Género  ", font=("Impact", 17))
    labelGenero.grid(row=2, column=0, padx=10, pady=8, sticky="ew")

    labelFacultad = tk.Label(frame, text="  Facultad  ", font=("Impact", 17))
    labelFacultad.grid(row=3, column=0, padx=10, pady=8, sticky="ew")

    labelElo = tk.Label(frame, text="  Elo  ", font=("Impact", 17))
    labelElo.grid(row=4, column=0, padx=10, pady=8, sticky="ew")

    labelVictorias = tk.Label(frame, text="  Victorias  ", font=("Impact", 17))
    labelVictorias.grid(row=5, column=0, padx=10, pady=8, sticky="ew")

    labelTorneos = tk.Label(frame, text="  Torneos  ", font=("Impact", 17))
    labelTorneos.grid(row=6, column=0, padx=10, pady=8, sticky="ew")

    labelTorneos = tk.Label(frame, text="  Medallas  ", font=("Impact", 17))
    labelTorneos.grid(row=7, column=0, padx=10, pady=8, sticky="ew")

    entryNombreCompleto = tk.Entry(frame, font=("Impact", 16))
    entryNombreCompleto.grid(row=1, column=1, padx=10, pady=8, sticky="ew")
    entryNombreCompleto.focus()

    menuGeneros = tk.Menubutton(frame, text="Masculino", font=("Impact", 16))
    menuGeneros.grid(row=2, column=1, padx=10, pady=8, sticky="ew")
    menuGenero = tk.Menu(menuGeneros, tearoff=0)
    menuGeneros.config(menu=menuGenero)
    menuGenero.add_command(label="Masculino", command=lambda:menuGeneros.config(text="Masculino"))
    menuGenero.add_command(label="Femenino", command=lambda:menuGeneros.config(text="Femenino"))

    menuFacultades = tk.Menubutton(frame, text="Ingeniería", font=("Impact", 16))
    menuFacultades.grid(row=3, column=1, padx=10, pady=8, sticky="ew")
    menuFacultad = tk.Menu(menuFacultades, tearoff=0)
    menuFacultades.config(menu=menuFacultad)
    menuFacultad.add_command(label="Ingeniería", command=lambda:menuFacultades.config(text="Ingeniería"))
    menuFacultad.add_command(label="Odontología", command=lambda:menuFacultades.config(text="Odontología"))
    menuFacultad.add_command(label="Arquitectura", command=lambda:menuFacultades.config(text="Arquitectura"))
    menuFacultad.add_command(label="Derecho", command=lambda:menuFacultades.config(text="Derecho"))
    menuFacultad.add_command(label="Sociales", command=lambda:menuFacultades.config(text="Sociales"))
    menuFacultad.add_command(label="Invitado", command=lambda:menuFacultades.config(text="Invitado"))
    menuFacultad.add_command(label="UJAP", command=lambda:menuFacultades.config(text="UJAP"))

    spinboxElo = tk.Spinbox(frame, from_=1000, to=3000, increment=50, font=("Impact", 16))
    spinboxElo.grid(row=4, column=1, padx=10, pady=8, sticky="ew")

    spinboxVictorias= tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxVictorias.grid(row=5, column=1, padx=10, pady=8, sticky="ew")

    spinboxTorneos = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxTorneos.grid(row=6, column=1, padx=10, pady=8, sticky="ew")

    spinboxMedallas = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxMedallas.grid(row=7, column=1, padx=10, pady=8, sticky="ew")

    botonLimpiar = tk.Button(frame, text="  Limpiar  ", font=("Impact", 17), command=limpiar) 
    botonLimpiar.grid(row=8, column=0, padx=10, pady=8, sticky="ew")

    botonAgregar = tk.Button(frame, text="  Agregar  ", font=("Impact", 17),  command=crearJugador)
    botonAgregar.grid(row=8, column=1, padx=10, pady=8, sticky="ew")

def interfazJugadores3(ventana, funcion, nombreJugador, gen, fac, el, vict, torn, meda):
    #Funciones
    def insertarDatos():
        entryNombreCompleto.insert(0, nombreJugador)
        if gen == "M":
            menuGeneros.config(text="Masculino")
        else:
            menuGeneros.config(text="Femenino")

        menuFacultades.config(text=fac)
        spinboxElo.delete(0, tk.END)
        spinboxVictorias.delete(0, tk.END)
        spinboxTorneos.delete(0, tk.END)
        spinboxMedallas.delete(0, tk.END) 
        spinboxElo.insert(0, el)
        spinboxVictorias.insert(0, vict)
        spinboxTorneos.insert(0, torn)
        spinboxMedallas.insert(0, meda)
        entryNombreCompleto.focus()
        
    def editarJugador():
        if vl.validarNombre(entryNombreCompleto.get()) and len(entryNombreCompleto.get()) <= 20:
            nombreCompleto = entryNombreCompleto.get()
        else:
            messagebox.showwarning("Advertencia", f" !El nombre solo debe tener caracteres alfanúmericos! \n Maximo 20 caracteres")
            return
        
        genero = menuGeneros.cget("text")

        facultad = menuFacultades.cget("text")
    
        if vl.validarEntero(spinboxElo.get()) and len(vl.validarEntero2(spinboxElo.get())) == 4:
            elo = spinboxElo.get()
        else:
            messagebox.showwarning("Advertencia", f"!El elo debe ser un numero entero positivo de 4 dígitos!")
            return
        
        if vl.validarEntero(spinboxVictorias.get()) and len(vl.validarEntero2(spinboxVictorias.get())) <= 2:
            victorias = spinboxVictorias.get()
        else:
            messagebox.showwarning("Advertencia", f"!El número de victorias debe ser un numero entero positivo de máximo 2 dígitos!")
            return
        
        if vl.validarEntero(spinboxTorneos.get()) and len(vl.validarEntero2(spinboxTorneos.get())) <= 2:
            torneos = spinboxTorneos.get()
        else:
            messagebox.showwarning("Advertencia", f"!El número de torneos debe ser un numero entero positivo de máximo 2 dígitos!")
            return
        
        if vl.validarEntero(spinboxMedallas.get()) and len(vl.validarEntero2(spinboxMedallas.get())) <= 2:
            if int(spinboxMedallas.get()) <= int(spinboxTorneos.get()):
                medallas = spinboxMedallas.get()
            else:
                messagebox.showwarning("Advertencia", f"!El número de medallas debe ser menor o igual al número de torneos!")
                return
        else:
            messagebox.showwarning("Advertencia", f"!El número de medallas debe ser un numero entero positivo de máximo 2 dígitos!")
            return

        respuesta = bd.editarDatosJugador(nombreJugador, nombreCompleto, genero[0], facultad, elo, victorias, torneos, medallas)
        if respuesta == True:
            messagebox.showwarning("Advertencia", f" !Ya existe un jugador con ese nombre! \n Por favor ingrese uno nuevo")
            return

        ventana.attributes('-disabled', False)
        ventanaJugadores3.destroy()
        funcion()
    
    def limpiar():
        entryNombreCompleto.delete(0, tk.END) 
        menuFacultades.config(text="Ingeniería")
        menuGeneros.config(text="Masculino")
        spinboxElo.delete(0, tk.END)
        spinboxVictorias.delete(0, tk.END) 
        spinboxTorneos.delete(0, tk.END) 
        spinboxMedallas.delete(0, tk.END) 
        entryNombreCompleto.focus()

    #Ventana
    ventanaJugadores3 = tk.Toplevel(ventana)
    ventanaJugadores3.title("ChessPyter")
    anchoVentana = 550
    altoVentana = 550
    x = (ventanaJugadores3.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaJugadores3.winfo_screenheight() - altoVentana)//2
    ventanaJugadores3.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y-50}")
    ventanaJugadores3.resizable(False, False)
    ventanaJugadores3.focus_force()
    ventanaJugadores3.grab_set()
    ventanaJugadores3.configure(bg="lightgray")
    ventanaJugadores3.bind("<Escape>", lambda e:(ventana.attributes('-disabled', False), ventanaJugadores3.destroy()))
    ventanaJugadores3.bind("<Return>", lambda e: editarJugador())
    ventanaJugadores3.protocol("WM_DELETE_WINDOW", lambda: (ventanaJugadores3.destroy(), sys.exit(0)))
    ventana.attributes('-disabled', True)

    #Widgets
    labelTitulo = tk.Label(ventanaJugadores3, text="Editar Jugador", font=("Impact", 20))
    labelTitulo.pack(pady= (20,10))

    frame = tk.Frame(ventanaJugadores3, bd=10, bg="gray", width=500, height=500)
    frame.pack()

    labelNombreCompleto = tk.Label(frame, text="  Nombre y Apellido  ", font=("Impact", 17))
    labelNombreCompleto.grid(row=1, column=0, padx=10, pady=8, sticky="ew")

    labelGenero = tk.Label(frame, text="  Género  ", font=("Impact", 17))
    labelGenero.grid(row=2, column=0, padx=10, pady=8, sticky="ew")

    labelFacultad = tk.Label(frame, text="  Facultad  ", font=("Impact", 17))
    labelFacultad.grid(row=3, column=0, padx=10, pady=8, sticky="ew")

    labelElo = tk.Label(frame, text="  Elo  ", font=("Impact", 17))
    labelElo.grid(row=4, column=0, padx=10, pady=8, sticky="ew")

    labelVictorias = tk.Label(frame, text="  Victorias  ", font=("Impact", 17))
    labelVictorias.grid(row=5, column=0, padx=10, pady=8, sticky="ew")

    labelTorneos = tk.Label(frame, text="  Torneos  ", font=("Impact", 17))
    labelTorneos.grid(row=6, column=0, padx=10, pady=8, sticky="ew")

    labelTorneos = tk.Label(frame, text="  Medallas  ", font=("Impact", 17))
    labelTorneos.grid(row=7, column=0, padx=10, pady=8, sticky="ew")

    entryNombreCompleto = tk.Entry(frame, font=("Impact", 16))
    entryNombreCompleto.grid(row=1, column=1, padx=10, pady=8, sticky="ew")
    entryNombreCompleto.focus()

    menuGeneros = tk.Menubutton(frame, text="Masculino", font=("Impact", 16))
    menuGeneros.grid(row=2, column=1, padx=10, pady=8, sticky="ew")
    menuGenero = tk.Menu(menuGeneros, tearoff=0)
    menuGeneros.config(menu=menuGenero)
    menuGenero.add_command(label="Masculino", command=lambda:menuGeneros.config(text="Masculino"))
    menuGenero.add_command(label="Femenino", command=lambda:menuGeneros.config(text="Femenino"))

    menuFacultades = tk.Menubutton(frame, text="Ingeniería", font=("Impact", 16))
    menuFacultades.grid(row=3, column=1, padx=10, pady=8, sticky="ew")
    menuFacultad = tk.Menu(menuFacultades, tearoff=0)
    menuFacultades.config(menu=menuFacultad)
    menuFacultad.add_command(label="Ingeniería", command=lambda:menuFacultades.config(text="Ingeniería"))
    menuFacultad.add_command(label="Odontología", command=lambda:menuFacultades.config(text="Odontología"))
    menuFacultad.add_command(label="Arquitectura", command=lambda:menuFacultades.config(text="Arquitectura"))
    menuFacultad.add_command(label="Derecho", command=lambda:menuFacultades.config(text="Derecho"))
    menuFacultad.add_command(label="Sociales", command=lambda:menuFacultades.config(text="Sociales"))
    menuFacultad.add_command(label="Invitado", command=lambda:menuFacultades.config(text="Invitado"))
    menuFacultad.add_command(label="UJAP", command=lambda:menuFacultades.config(text="UJAP"))

    spinboxElo = tk.Spinbox(frame, from_=1000, to=3000, increment=50, font=("Impact", 16))
    spinboxElo.grid(row=4, column=1, padx=10, pady=8, sticky="ew")

    spinboxVictorias= tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxVictorias.grid(row=5, column=1, padx=10, pady=8, sticky="ew")

    spinboxTorneos = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxTorneos.grid(row=6, column=1, padx=10, pady=8, sticky="ew")

    spinboxMedallas = tk.Spinbox(frame, from_=0, to=99, font=("Impact", 16))
    spinboxMedallas.grid(row=7, column=1, padx=10, pady=8, sticky="ew")

    botonLimpiar = tk.Button(frame, text="  Limpiar  ", font=("Impact", 17), command=limpiar) 
    botonLimpiar.grid(row=8, column=0, padx=10, pady=8, sticky="ew")

    botonEditar = tk.Button(frame, text="  Editar ", font=("Impact", 17),  command=editarJugador)
    botonEditar.grid(row=8, column=1, padx=10, pady=8, sticky="ew")

    insertarDatos()

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



