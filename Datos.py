import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkinter import ttk, messagebox
import sys

def interfazDatos1(ventanaMain):
    #Funciones
    def cargarJugadores():
        filtro = botonFiltrar.cget("text")
        if filtro == "Femenino":
            botonFiltrar.config(text="General")
        else:
            botonFiltrar.config(text="Femenino")

        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosRanking(filtro)

        if len(datos) > 0:
            labelJugadores.config(text=f"Jugadores: {len(datos)}")
        else:
            labelJugadores.config(text=f"Jugadores: 0")
            return
        
        tag = ""
        posicion = 1
        for registro in datos:
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
            
            tabla.insert("", tk.END, values=(posicion, registro[0], registro[2], registro[3], registro[4]), tags=(tag))
            posicion += 1
            
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    """   def actualizarLista():
        print("Actualizando lista de jugadores...")
        for dato in tabla.get_children():
            tabla.delete(dato)
        cargarJugadores()"""

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    #Ventana
    ventanaDatos1 = tk.Toplevel(ventanaMain)
    ventanaDatos1.title("Datos")
    anchoVentana = 550
    altoVentana = 375
    x = (ventanaDatos1.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos1.winfo_screenheight() - altoVentana)//2
    ventanaDatos1.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos1.focus_force()
    ventanaDatos1.grab_set()
    ventanaDatos1.resizable(False, False)
    ventanaDatos1.configure(bg="lightgray")
    ventanaDatos1.bind("<Escape>", lambda e:(ventanaMain.deiconify(), ventanaDatos1.destroy()))
    ventanaDatos1.bind("<Double-Button-1>", lambda e:desseleccionarFila())
    ventanaDatos1.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos1.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos1, text=f"Ranking", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos1, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("#","Nombre y Apellido", "Facultad", "Elo", "Victorias"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

    tabla.column("#", anchor=tk.CENTER, width=30)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Facultad", anchor=tk.CENTER, width=95)
    tabla.column("Elo", anchor=tk.CENTER, width=50)
    tabla.column("Victorias", anchor=tk.CENTER, width=70)

    tabla.heading("#", text="#")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Elo", text="Elo")
    tabla.heading("Victorias", text="Victorias")

    botonFiltrar = tk.Button(ventanaDatos1, text="General", font=20,  command= cargarJugadores)
    botonFiltrar.pack(padx=10, pady=10, side=tk.RIGHT)

    labelJugadores = tk.Label(ventanaDatos1, text="Jugadores: 0", bg="lightgray", fg="black", font=15)
    labelJugadores.pack(padx=10, pady=10, side=tk.LEFT)

    cargarJugadores()

def interfazDatos2(ventanaMain):
    #Funciones
    def cargarTorneos():
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosListaTorneos()

        if len(datos) > 0:
            labelTorneos.config(text=f"Torneos: {len(datos)}")
        else:
            labelTorneos.config(text=f"Torneos: 0")
            return

        for registro in datos:
            """   if registro[2] == "Ingeniería":
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
            tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")"""
                                               #nombre, fecha, participantes, rondas, invitados, descripcion
            tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5]))
            
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    """   def actualizarLista():
        print("Actualizando lista de jugadores...")
        for dato in tabla.get_children():
            tabla.delete(dato)
        cargarJugadores()"""

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    #Ventana
    ventanaDatos2 = tk.Toplevel(ventanaMain)
    ventanaDatos2.title("Datos")
    anchoVentana = 700
    altoVentana = 350
    x = (ventanaDatos2.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos2.winfo_screenheight() - altoVentana)//2
    ventanaDatos2.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos2.focus_force()
    ventanaDatos2.grab_set()
    ventanaDatos2.resizable(False, False)
    ventanaDatos2.configure(bg="lightgray")
    ventanaDatos2.bind("<Escape>", lambda e:(ventanaMain.deiconify(), ventanaDatos2.destroy()))
    ventanaDatos2.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaDatos2.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos2.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos2, text=f"Torneos", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos2, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("Nombre", "Fecha", "Participantes", "Rondas", "Invitados", "Descripción"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

    tabla.column("Nombre", anchor=tk.CENTER, width=150)
    tabla.column("Fecha", anchor=tk.CENTER, width=100)
    tabla.column("Participantes", anchor=tk.CENTER, width=100)
    tabla.column("Rondas", anchor=tk.CENTER, width=65)
    tabla.column("Invitados", anchor=tk.CENTER, width=75)
    tabla.column("Descripción", anchor=tk.CENTER, width=150)

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Participantes", text="Participantes")
    tabla.heading("Rondas", text="Rondas")
    tabla.heading("Invitados", text="Invitados")
    tabla.heading("Descripción", text="Descripción")

    labelTorneos = tk.Label(ventanaDatos2, text="Torneos: 0", bg="lightgray", fg="black", font=15)
    labelTorneos.pack(padx=10, pady=10, side=tk.LEFT)

    cargarTorneos()

def interfazDatos3(ventanaMain):
    #Funciones
    def cargarTabla():
        datos = bd.consultarDatosJugadores("Medallas")
        #bd.eliminarDatosMedallas()
        for registro in datos:
            bd.agregarDatosMedallas(registro)
        cargarJugadores()

    def cargarJugadores():
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosMedallas()

        if len(datos) > 0:
            labeljugadores.config(text=f"Jugadores: {len(datos)}")
        else:
            labeljugadores.config(text=f"Jugadores: 0")
            return
        
        tag = ""
        posicion = 1
        for registro in datos:
            if registro[1] == "Ingeniería":
                tag = "Ingeniería"
            elif registro[1] == "Sociales":
                tag = "Sociales"
            elif registro[1] == "Arquitectura":
                tag = "Arquitectura"
            elif registro[1] == "Derecho":
                tag = "Derecho"
            elif registro[1] == "Odontología":
                tag = "Odontología"
            elif registro[1] == "Invitado":
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
                                                #       #nombre,     facultad,     torneos,    medallas,     oro,        plata,       bronce,       otra,                                        estado
            tabla.insert("", tk.END, values=(posicion, registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], (f"{"✔" if (int(registro[4]) + int(registro[5]) + int(registro[6]) + int(registro[7])) == registro[3] else "✖"}")), tags=(tag))
            posicion += 1
            
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=6, sticky="ns")
    
    """   def actualizarLista():
        print("Actualizando lista de jugadores...")
        for dato in tabla.get_children():
            tabla.delete(dato)
        cargarJugadores()"""
    
    def menu(evento):
        fila = tabla.identify_row(evento.y)
        if fila:
            tabla.selection_set(fila)
            menu.tk_popup(evento.x_root, evento.y_root)
    
    def editarFila():
        fila = tabla.selection()
        datos = tabla.item(fila, 'values')
        ventanaDatos3.withdraw()
        interfazDatos4(ventanaMain, datos[1], datos[3], datos[4], datos[5], datos[6], datos[7], datos[8])

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    #Ventana
    ventanaDatos3 = tk.Toplevel(ventanaMain)
    ventanaDatos3.title("Datos")
    anchoVentana = 800
    altoVentana = 350
    x = (ventanaDatos3.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos3.winfo_screenheight() - altoVentana)//2
    ventanaDatos3.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos3.focus_force()
    ventanaDatos3.grab_set()
    ventanaDatos3.resizable(False, False)
    ventanaDatos3.configure(bg="lightgray")
    ventanaDatos3.bind("<Escape>", lambda e:(ventanaMain.deiconify(), ventanaDatos3.destroy()))
    ventanaDatos3.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaDatos3.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos3.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos3, text=f"Medallas", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos3, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 20, rowheight=20)
    tabla = ttk.Treeview(frame, columns=("#", "Nombre y Apellido", "Facultad", "Torneos", "Medallas", "Oro", "Plata", "Bronce", "Otra", "Estado"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")
    tabla.bind("<Button-3>", menu)

    tabla.column("#", anchor=tk.CENTER, width=40)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=150)
    tabla.column("Facultad", anchor=tk.CENTER, width=95)
    tabla.column("Torneos", anchor=tk.CENTER, width=70)
    tabla.column("Medallas", anchor=tk.CENTER, width=75)
    tabla.column("Oro", anchor=tk.CENTER, width=50)
    tabla.column("Plata", anchor=tk.CENTER, width=60)
    tabla.column("Bronce", anchor=tk.CENTER, width=60)
    tabla.column("Otra", anchor=tk.CENTER, width=55)
    tabla.column("Estado", anchor=tk.CENTER, width=60)

    tabla.heading("#", text="#")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Facultad", text="Facultad")
    tabla.heading("Torneos", text="Torneos")
    tabla.heading("Medallas", text="Medallas")
    tabla.heading("Oro", text="Oro")
    tabla.heading("Plata", text="Plata")
    tabla.heading("Bronce", text="Bronce")
    tabla.heading("Otra", text="Otra")
    tabla.heading("Estado", text="Estado")

    menu = tk.Menu(ventanaDatos3, tearoff=0)
    menu.add_command(label="Editar", command=editarFila)

    labeljugadores = tk.Label(ventanaDatos3, text="Jugadores: 0", bg="lightgray", fg="black", font=15)
    labeljugadores.pack(padx=10, pady=10, side=tk.LEFT)

    cargarTabla()

def interfazDatos4(ventanaMain, nombreJugador, torneos, medall, o, pla, bro, otr):
    #Funciones
    def insertarDatos():
        spinboxMedallas.delete(0, tk.END)
        spinboxOro.delete(0, tk.END)
        spinboxPlata.delete(0, tk.END)
        spinboxBronce.delete(0, tk.END)
        spinboxOtra.delete(0, tk.END)
        spinboxMedallas.insert(0, medall)
        spinboxOro.insert(0, o)
        spinboxPlata.insert(0, pla)
        spinboxBronce.insert(0, bro)
        spinboxOtra.insert(0, otr)

    def editarMedallas():
        if vl.validarEntero(spinboxMedallas.get()):
            medallas = spinboxMedallas.get()
        else:
            labelError.config(text="!!La cantidad de medallas debe ser \n un numero entero mayor a 0 y menor a 100!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return    

        if vl.validarEntero(spinboxOro.get()):
            oro = spinboxOro.get()
        else:
            labelError.config(text="!!La cantidad de medallas(Oro) debe ser \n un numero entero mayor a 0 y menor a 100!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        if vl.validarEntero(spinboxPlata.get()):
            plata = spinboxPlata.get()
        else:
            labelError.config(text="!!La cantidad de medallas(Plata) debe ser \n un numero entero mayor a 0 y menor a 100!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return    
        
        if vl.validarEntero(spinboxBronce.get()):
            bronce = spinboxBronce.get()
        else:
            labelError.config(text="!!La cantidad de medallas(Bronce) debe ser \n un numero entero mayor a 0 y menor a 100!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return 
        
        if vl.validarEntero(spinboxOtra.get()):
            otra = spinboxOtra.get()
        else:
            labelError.config(text="!!La cantidad de medallas(Otra) debe ser un \n numero entero mayor a 0 y menor a 100!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return 
    
        medallasTotales = int(oro) + int(plata) + int(bronce) + int(otra)
        if medallasTotales != int(medallas) :
            labelError.config(text=f"!!La cantidad de medallas \n (Oro + Plata + Bronce + Otra) debe ser \n igual al numero de Medallas totales [{medallas}]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        if  int(medallas) > int(torneos):
            labelError.config(text=f"!!El número de medallas debe ser \n menor o igual al número de torneos!! [{torneos}]!!", bg="lightgray", font=10)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return

        bd.actualizarMedallasJugador(nombreJugador, medallas, oro, plata, bronce, otra)
        ventanaDatos4.destroy()
        interfazDatos3(ventanaMain)

    def limpiar():
        spinboxMedallas.delete(0, tk.END)
        spinboxOro.delete(0, tk.END)
        spinboxPlata.delete(0, tk.END)
        spinboxBronce.delete(0, tk.END)
        spinboxOtra.delete(0, tk.END)
        spinboxMedallas.focus()

    #Ventana
    ventanaDatos4 = tk.Toplevel(ventanaMain)
    ventanaDatos4.title("Datos")
    anchoVentana = 375
    altoVentana = 425
    x = (ventanaDatos4.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos4.winfo_screenheight() - altoVentana)//2
    ventanaDatos4.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos4.grab_set()
    ventanaDatos4.focus_force()
    ventanaDatos4.resizable(False, False)
    ventanaDatos4.configure(bg="lightgray")
    ventanaDatos4.bind("<Escape>", lambda e:(ventanaDatos4.destroy(), interfazDatos3(ventanaMain)))
    ventanaDatos4.bind("<Return>", lambda e: editarMedallas())
    ventanaDatos4.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos4.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos4, text="Editar Medallas", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos4, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelMedallas = tk.Label(frame, text="Medallas", font= 20)
    labelMedallas.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelOro = tk.Label(frame, text="Oro", font= 20)
    labelOro.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelPlata = tk.Label(frame, text="Plata", font= 20)
    labelPlata.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    labelBronce = tk.Label(frame, text="Bronce", font= 20)
    labelBronce.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    labelOtra = tk.Label(frame, text="Otra", font= 20)
    labelOtra.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    spinboxMedallas = tk.Spinbox(frame, from_=0, to=99, font=20)
    spinboxMedallas.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    ventanaDatos4.after(10, lambda:spinboxMedallas.focus())

    spinboxOro = tk.Spinbox(frame, from_=0, to=99, font=20)
    spinboxOro.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    spinboxPlata = tk.Spinbox(frame, from_=0, to=99, font=20)
    spinboxPlata.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    spinboxBronce = tk.Spinbox(frame, from_=0, to=99, font=20)
    spinboxBronce.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    spinboxOtra = tk.Spinbox(frame, from_=0, to=99, font=20)
    spinboxOtra.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=limpiar)
    botonLimpiar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="Editar", font=20,  command=editarMedallas)
    botonEditar.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    insertarDatos()

#Cargar jugadores con medallas de la tabla Jugadores a la tabla Medallas
#Al momento de crear un Jugador con medalla se agrege automaticamente al la tabla Medallas
#Al terminar un torneo y haya un jugador sin medallas que ganó una en ese torneo, ese jugador se agrega a la tabla Jugadores
def rankingGeneral():
    pass

def rankingFemenino():
    pass

def filtarRanking():
    pass

def listaTorneos():
    pass

def Medallas():
    pass
