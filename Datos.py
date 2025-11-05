import tkinter as tk
import baseDatos as bd
import validaciones as vl
from tkcalendar import DateEntry
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
        posiciones = 1
        femenina = True
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

            tabla.tag_configure("Oro", background="#DEDE2C", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Plata", background="#545050", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Bronce", background="#8D4416", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Femenina", background="#DE2C50", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Ingeniería", background="#00008B", foreground="#FFFFFF")
            tabla.tag_configure("Sociales", background="#A52A2A", foreground="#FFFFFF")
            tabla.tag_configure("Arquitectura", background="#402169", foreground="#FFFFFF")
            tabla.tag_configure("Derecho", background="#000000", foreground="#FFFFFF")
            tabla.tag_configure("Odontología", background="#888888", foreground="#FFFFFF")
            tabla.tag_configure("Invitado", background="#73bf00", foreground="#FFFFFF")
            tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")

            if posiciones <= 3:
                if posiciones == 1:
                    tag = "Oro"
                elif posiciones == 2:
                    tag = "Plata"
                else:
                    tag = "Bronce"
            elif registro[1] == "F" and femenina:
                tag = "Femenina"
                femenina = False
            
            tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], registro[3], registro[4]), tags=(tag))
            posiciones += 1
            
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
    anchoVentana = 600
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
    tabla = ttk.Treeview(frame, columns=("#","Nombre y Apellido", "Género", "Facultad", "Elo", "Victorias"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

    tabla.column("#", anchor=tk.CENTER, width=30)
    tabla.column("Nombre y Apellido", anchor=tk.CENTER, width=200)
    tabla.column("Género", anchor=tk.CENTER, width=70)
    tabla.column("Facultad", anchor=tk.CENTER, width=95)
    tabla.column("Elo", anchor=tk.CENTER, width=50)
    tabla.column("Victorias", anchor=tk.CENTER, width=70)

    tabla.heading("#", text="#")
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido")
    tabla.heading("Género", text="Género")
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
    def cargarTorneos(filtro="Fecha"):
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosListaTorneos(filtro)

        if len(datos) > 0:
            labelTorneos.config(text=f"Torneos: {len(datos)}")
        else:
            labelTorneos.config(text=f"Torneos: 0")
            return

        for registro in datos:
                                               #nombre,     fecha,    participantes,  rondas,    invitados,   descripcion
            tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], registro[4], (f"{registro[5] if registro[5] != "" else "Ninguna"}")))
            
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
        datosTorneo = (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
        nombreTorneo = f"{datos[0]}_{datos[1]}_P{datos[2]}_R{datos[3]}_{datos[4]}{"_" if datos[5] != "Ninguna" else ""}{datos[5] if datos[5] != "Ninguna" else ""}"
        ventanaDatos2.withdraw()
        interfazDatos6(ventanaMain, nombreTorneo, datosTorneo)


    def borrarTorneo():
        item = tabla.selection()
        valores = tabla.item(item, 'values')
        respuesta = messagebox.askyesno("Borrar", f"¿Estás seguro de borrar \n el torneo {valores[0]}?")
        if respuesta:
            tabla.delete(item)
            bd.eliminarTorneo(valores[0]) 
            cargarTorneos()
    
    def verTorneo():
        fila = tabla.selection()
        datos = tabla.item(fila, 'values')
        datosTorneo = (datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
        nombreTorneo = f"{datos[0]}_{datos[1]}_P{datos[2]}_R{datos[3]}_{datos[4]}{"_" if datos[5] != "Ninguna" else ""}{datos[5] if datos[5] != "Ninguna" else ""}"
        ventanaDatos2.withdraw()
        interfazDatos5(ventanaMain, nombreTorneo, datosTorneo)

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
    tabla.bind("<Button-3>", menu)

    tabla.column("Nombre", anchor=tk.CENTER, width=150)
    tabla.column("Fecha", anchor=tk.CENTER, width=100)
    tabla.column("Participantes", anchor=tk.CENTER, width=100)
    tabla.column("Rondas", anchor=tk.CENTER, width=65)
    tabla.column("Invitados", anchor=tk.CENTER, width=75)
    tabla.column("Descripción", anchor=tk.CENTER, width=150)

    tabla.heading("Nombre", text="Nombre", command=lambda:cargarTorneos("Nombre"))
    tabla.heading("Fecha", text="Fecha", command=lambda:cargarTorneos())
    tabla.heading("Participantes", text="Participantes", command=lambda:cargarTorneos("Participantes"))
    tabla.heading("Rondas", text="Rondas", command=lambda:cargarTorneos("Rondas"))
    tabla.heading("Invitados", text="Invitados", command=lambda:cargarTorneos("Invitados"))
    tabla.heading("Descripción", text="Descripción", command=lambda:cargarTorneos("Descripcion"))

    menu = tk.Menu(ventanaDatos2, tearoff=0)
    menu.add_command(label="Ver", command=verTorneo)
    menu.add_command(label="Editar", command=editarFila)
    menu.add_command(label="Borrar", command=borrarTorneo)

    labelTorneos = tk.Label(ventanaDatos2, text="Torneos: 0", bg="lightgray", fg="black", font=15)
    labelTorneos.pack(padx=10, pady=10, side=tk.LEFT)

    cargarTorneos()

def interfazDatos3(ventanaMain):
    #Funciones
    def cargarTabla():
        datos = bd.consultarDatosJugadores()
        for registro in datos:
            bd.agregarDatosMedallas(registro)
        cargarJugadores()

    def cargarJugadores(filtro="#"):
        for fila in tabla.get_children():
            tabla.delete(fila)
        datos = bd.consultarDatosMedallas(filtro)

        if len(datos) > 0:
            labeljugadores.config(text=f"Jugadores: {len(datos)}")
        else:
            labeljugadores.config(text=f"Jugadores: 0")
            return
        
        tag = ""
        posiciones = 1
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

            tabla.tag_configure("Oro", background="#DEDE2C", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Plata", background="#545050", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Bronce", background="#8D4416", foreground="#FFFFFF", font=("", 11, "bold"))
            tabla.tag_configure("Ingeniería", background="#00008B", foreground="#FFFFFF")
            tabla.tag_configure("Sociales", background="#A52A2A", foreground="#FFFFFF")
            tabla.tag_configure("Arquitectura", background="#402169", foreground="#FFFFFF")
            tabla.tag_configure("Derecho", background="#000000", foreground="#FFFFFF")
            tabla.tag_configure("Odontología", background="#888888", foreground="#FFFFFF")
            tabla.tag_configure("Invitado", background="#73bf00", foreground="#FFFFFF")
            tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")

            if posiciones <= 3:
                if posiciones == 1:
                    tag = "Oro"
                elif posiciones == 2:
                    tag = "Plata"
                else:
                    tag = "Bronce"   
                                                #       #nombre,     facultad,     torneos,    medallas,     oro,        plata,       bronce,       otra,                                        estado
            tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], registro[6], registro[7], (f"{"✔" if (int(registro[4]) + int(registro[5]) + int(registro[6]) + int(registro[7])) == registro[3] else "✖"}")), tags=(tag))
            posiciones += 1
            
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

    tabla.heading("#", text="#", command=lambda:cargarJugadores())
    tabla.heading("Nombre y Apellido", text="Nombre y Apellido", command=lambda:cargarJugadores("Nombre"))
    tabla.heading("Facultad", text="Facultad", command=lambda:cargarJugadores("Facultad"))
    tabla.heading("Torneos", text="Torneos", command=lambda:cargarJugadores("Torneos"))
    tabla.heading("Medallas", text="Medallas", command=lambda:cargarJugadores("Medallas"))
    tabla.heading("Oro", text="Oro", command=lambda:cargarJugadores("Oro"))
    tabla.heading("Plata", text="Plata", command=lambda:cargarJugadores("Plata"))
    tabla.heading("Bronce", text="Bronce", command=lambda:cargarJugadores("Bronce"))
    tabla.heading("Otra", text="Otra", command=lambda:cargarJugadores("Otra"))
    tabla.heading("Estado", text="Estado", command=lambda:cargarJugadores("Estado"))

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

def interfazDatos5(ventanaMain, nombreTorneo, datosTorneo):
    #Funciones
    def cargarTabla():
        for fila in tabla.get_children():
            tabla.delete(fila)

        if botonCambio.cget("text") == "Despues Torneo":
            datos = bd.consultarDatosAntesTorneo("AT_"+nombreTorneo)
        else:
            datos = bd.consultarDatosDespuesTorneo("DT_"+nombreTorneo)

        if datos == None:
            ventanaDatos5.destroy()
            interfazDatos2(ventanaMain)
            messagebox.showerror("Error", "!!Torneo no encontrado!!")
            return
        
        if botonCambio.cget("text") == "Despues Torneo":
            tabla.column("Col1", anchor=tk.CENTER, width=180)
            tabla.column("Col2", anchor=tk.CENTER, width=70)
            tabla.column("Col3", anchor=tk.CENTER, width=95)
            tabla.column("Col4", anchor=tk.CENTER, width=45)
            tabla.column("Col5", anchor=tk.CENTER, width=75)
            tabla.column("Col6", anchor=tk.CENTER, width=75)
            tabla.column("Col7", anchor=tk.CENTER, width=75)
            tabla.column("Col8", anchor=tk.CENTER, width=60)
            tabla.column("Col9", anchor=tk.CENTER, width=110)
            
            tabla.heading("Col1", text="Nombre y Apellido")
            tabla.heading("Col2", text="Genero")
            tabla.heading("Col3", text="Facultad")
            tabla.heading("Col4", text="Elo")
            tabla.heading("Col5", text="Victorias")
            tabla.heading("Col6", text="Tablas")
            tabla.heading("Col7", text="Derrotas")
            tabla.heading("Col8", text="Puntos")
            tabla.heading("Col9", text="Desempates")
        else:
            tabla.column("Col1", anchor=tk.CENTER, width=35)
            tabla.column("Col2", anchor=tk.CENTER, width=175)
            tabla.column("Col3", anchor=tk.CENTER, width=70)
            tabla.column("Col4", anchor=tk.CENTER, width=95)
            tabla.column("Col5", anchor=tk.CENTER, width=60)
            tabla.column("Col6", anchor=tk.CENTER, width=110)
            tabla.column("Col7", anchor=tk.CENTER, width=85)
            tabla.column("Col8", anchor=tk.CENTER, width=95)
            tabla.column("Col9", anchor=tk.CENTER, width=100)
            
            tabla.heading("Col1", text="#")
            tabla.heading("Col2", text="Nombre y Apellido")
            tabla.heading("Col3", text="Genero")
            tabla.heading("Col4", text="Facultad")
            tabla.heading("Col5", text="Puntos")
            tabla.heading("Col6", text="Desempates")
            tabla.heading("Col7", text="Elo(+/-)")
            tabla.heading("Col8", text="Victorias(+)")
            tabla.heading("Col9", text="Medallas(+)")
        
        posiciones = 1
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

                tabla.tag_configure("Oro", background="#DEDE2C", foreground="#FFFFFF", font=("", 11, "bold"))
                tabla.tag_configure("Plata", background="#545050", foreground="#FFFFFF", font=("", 11, "bold"))
                tabla.tag_configure("Bronce", background="#8D4416", foreground="#FFFFFF", font=("", 11, "bold"))
                tabla.tag_configure("Femenina", background="#DE2C50", foreground="#FFFFFF", font=("", 11, "bold"))
                tabla.tag_configure("Ingeniería", background="#00008B", foreground="#FFFFFF")
                tabla.tag_configure("Sociales", background="#A52A2A", foreground="#FFFFFF")
                tabla.tag_configure("Arquitectura", background="#402169", foreground="#FFFFFF")
                tabla.tag_configure("Derecho", background="#000000", foreground="#FFFFFF")
                tabla.tag_configure("Odontología", background="#888888", foreground="#FFFFFF")
                tabla.tag_configure("Invitado", background="#73bf00", foreground="#FFFFFF")
                tabla.tag_configure("UJAP", background="#E54A27", foreground="#FFFFFF")
                
                if botonCambio.cget("text") == "Despues Torneo":
                    tabla.insert("", tk.END, values=(registro[0], registro[1], registro[2], registro[3], registro[4] , registro[5], registro[6], registro[7], (f"{registro[8]}  {registro[9]}")), tags=(tag))
                else:
                    if posiciones <= 3:
                        if posiciones == 1:
                            tag = "Oro"
                        elif posiciones == 2:
                            tag = "Plata"
                        else:
                            tag = "Bronce"                   #         Nombre       Genero      Facultad        Puntos                   Desempates             Elo       Victorias    Medallas
                        tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), registro[3], registro[4], registro[5]), tags=(tag))
                        posiciones += 1
                    elif femenino == True and registro[1] == "F":
                        tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), registro[3], registro[4], registro[5]), tags=(tag))
                        posiciones += 1
                        femenino = False
                    else:
                        tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), registro[3], registro[4], registro[5]), tags=(tag))
                        posiciones += 1
                
        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=10, sticky="ns")

    def desseleccionarFila():
        for fila in tabla.selection():
            tabla.selection_remove(fila)

    def verDatos():
        messagebox.showinfo("Información Torneo", f" Nombre: {datosTorneo[0]} \n Fecha: {datosTorneo[1]} \n Participantes: {datosTorneo[2]} \n Rondas: {datosTorneo[3]} \n Invitados: {"Si" if datosTorneo[4] == "True" else "No"} \n Descripción: {"Ninguna" if datosTorneo[5] == "" else datosTorneo[5]}")


    #Ventana
    ventanaDatos5 = tk.Toplevel(ventanaMain)
    ventanaDatos5.title("Torneo")
    anchoVentana = 850
    altoVentana = 450
    x = (ventanaDatos5.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos5.winfo_screenheight() - altoVentana)//2
    ventanaDatos5.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos5.focus_force()
    ventanaDatos5.grab_set()
    ventanaDatos5.resizable(False, False)
    ventanaDatos5.configure(bg="lightgray")
    ventanaDatos5.bind("<Escape>", lambda e:(ventanaDatos5.destroy(), interfazDatos2(ventanaMain)))
    ventanaDatos5.bind("<Double-Button-1>", lambda e: desseleccionarFila())
    ventanaDatos5.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos5.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos5, text=f"{datosTorneo[0]}", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos5, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    estilo = ttk.Style()
    estilo.configure("Treeview.Heading", font= 20)
    estilo.configure("Treeview", font= 15, rowheight=30)
    tabla = ttk.Treeview(frame, columns=("Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8", "Col9"),  show="headings")
    tabla.grid(row=0, column=0, columnspan=9, padx=5, pady=10, sticky="ew") 

    botonVerDatos = tk.Button(ventanaDatos5, text="Datos", bg="lightgray", font=15, command=verDatos)
    botonVerDatos.pack(padx=10, pady=10, side=tk.RIGHT)

    botonCambio = tk.Button(ventanaDatos5, text="Despues Torneo", bg="lightgray", font=20, command=lambda:(botonCambio.config(text=f"{"Antes Torneo" if botonCambio.cget("text") == "Despues Torneo" else "Despues Torneo"}"), cargarTabla()))
    botonCambio.pack(padx=10, pady=10, side=tk.RIGHT)

    cargarTabla()

def interfazDatos6(ventanaMain, nombreTorneo, datosTorneo):
    #Funciones
    #(nombre, fecha, participantes, rondas, invitados, descripcion)
    def insertarDatos():
        entryNombre.insert(0, datosTorneo[0])
        entryFecha.insert(0, datosTorneo[1])
        if datosTorneo[5] != "Ninguna":
            entryDescripcion.insert(0, datosTorneo[5])
        
    def editarTorneo():
        if vl.validarNombre(entryNombre.get()):
            nombre = entryNombre.get()
        else:
            labelError.config(text="!!El nombre solo debe tener caracteres \n alfanúmericos [Máximo 15]!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        fecha = str(entryFecha.get_date()).replace("-", "/")   

        if vl.validarTexto(entryDescripcion.get()):
            descripcion = entryDescripcion.get()
        else:
            labelError.config(text="!!La descripción no debe exceder \n los 15 caracteres!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        respuesta1 = bd.editarTablaAntesTorneo("AT_"+nombreTorneo, nombre, fecha, datosTorneo[2], datosTorneo[3], datosTorneo[4], descripcion)
        respuesta2 = bd.editarTablaDespuesTorneo("DT_"+nombreTorneo, nombre, fecha, datosTorneo[2], datosTorneo[3], datosTorneo[4], descripcion)
        bd.editarTablaListaTorneo(datosTorneo[0], nombre, fecha, descripcion)
        if respuesta1 == True or respuesta2 == True:
            labelError.config(text="!!Ya existe un torneo con estos datos \n por favor ingrese uno nuevo!!", bg="lightgray", font=12)
            labelError.after(3000, lambda:labelError.config(text="", bg="gray"))
            return
        
        labelError.config(text=f"!Torneo editado con exito!!", bg="lightgray", font=12)
        labelError.after(2000, lambda:(ventanaDatos6.destroy(), interfazDatos2(ventanaMain)))

    def limpiar():
        entryNombre.delete(0, tk.END)
        entryFecha.config(state="normal")
        entryFecha.set_date(None)
        entryFecha.config(state="readonly")
        entryDescripcion.delete(0, tk.END)
        entryNombre.focus()

    #Ventana
    ventanaDatos6 = tk.Toplevel(ventanaMain)
    ventanaDatos6.title("Torneo")
    anchoVentana = 400
    altoVentana = 325
    x = (ventanaDatos6.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaDatos6.winfo_screenheight() - altoVentana)//2
    ventanaDatos6.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    ventanaDatos6.grab_set()
    ventanaDatos6.focus_force()
    ventanaDatos6.resizable(False, False)
    ventanaDatos6.configure(bg="lightgray")
    ventanaDatos6.bind("<Escape>", lambda e:(ventanaDatos6.destroy(), interfazDatos2(ventanaMain)))
    ventanaDatos6.bind("<Return>", lambda e: editarTorneo())
    ventanaDatos6.protocol("WM_DELETE_WINDOW", lambda: (ventanaDatos6.destroy(), sys.exit(0)))

    #Widgets
    labelTitulo = tk.Label(ventanaDatos6, text="Editar Torneo", font= 20)
    labelTitulo.pack(pady= 10)

    frame = tk.Frame(ventanaDatos6, bd=10, bg="gray", width=500, height=500)
    frame.pack_propagate(False)
    frame.pack()
    frame.grid_columnconfigure(1, weight=1)

    labelNombre = tk.Label(frame, text="Nombre", font= 20)
    labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    labelFecha = tk.Label(frame, text="Fecha", font= 20)
    labelFecha.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    labelDescripcion = tk.Label(frame, text="Descripción", font= 20)
    labelDescripcion.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    entryNombre = tk.Entry(frame, font=20)
    entryNombre.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    ventanaDatos6.after(10, lambda:entryNombre.focus())

    entryFecha = DateEntry(frame, date_pattern='dd-mm-yy', bg="gray", font=20, state="readonly")
    entryFecha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entryDescripcion = tk.Entry(frame, font=20)
    entryDescripcion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    botonLimpiar = tk.Button(frame, text="Limpiar", font=20, command=limpiar)
    botonLimpiar.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    botonEditar = tk.Button(frame, text="Editar", font=20,  command=editarTorneo)
    botonEditar.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    labelError = tk.Label(frame, text="", bg="gray")
    labelError.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

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
