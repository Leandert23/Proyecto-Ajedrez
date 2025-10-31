import tkinter as tk
import baseDatos as bd
from tkinter import ttk, messagebox

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
                                                     #      [Nombre y Apellido], Genero, Facultad,                                                                                   Elo,                                                                                                                                      Victorias,                               Medallas,                Torneos, Puntos, Desempate1, Desempate2
                if posiciones <= 2:
                    tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}(+{estadisticasJugadores[indice][1]})"), (f"{registro[5]}(+1)")), tags=(tag))
                    posiciones += 1
                    participantes -= 1
                elif femenino == True and registro[1] == "F":
                    tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"),(f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}(+{estadisticasJugadores[indice][1]})"), (f"{registro[5]}(+1)")), tags=(tag))
                    posiciones += 1
                    participantes -= 1
                    femenino = False
                else:
                    tabla.insert("", tk.END, values=(posiciones+1, registro[0], registro[1], registro[2], registro[7], (f"{registro[8]}  {registro[9]}"), (f"{registro[3]}({"+" if int((estadisticasJugadores[indice][2]))+participantes > 0 else ""}{int(estadisticasJugadores[indice][2])+participantes})"), (f"{registro[4]}(+{estadisticasJugadores[indice][1]})"), registro[5]), tags=(tag))
                    posiciones += 1
                    participantes -= 1
                #tabla.insert("", tk.END, values=(posiciones, registro[0], registro[1], registro[2], (f"{registro[3] + estadisticasJugadores[0]}"), (f"{registro[4] + estadisticasJugadores[1]}"),(f"{registro[5] + estadisticasJugadores[1]}")), tags=(tag))
                                            #"#", "Nombre y Apellido", "Genero", "Facultad", "Elo(+/-)", "Victorias(+)", "Medallas(+)"

        if len(datos) > 10:
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
            tabla.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=10, sticky="ns")

    def desseleccionarFila(evento):
        for fila in tabla.selection():
            tabla.selection_remove(fila)
    
    def verDatos():
        messagebox.showinfo("Información Torneo:", f" Nombre: {datosTorneo[0]} \n Fecha: {datosTorneo[1]} \n Participantes: {datosTorneo[2]} \n Rondas: {datosTorneo[3]} \n Invitados: {"Si" if datosTorneo[4] == "True" else "No"} \n Descripción: {"Ninguna" if datosTorneo[5] == "" else datosTorneo[5]}")

    #Ventana
    ventanaTorneo6 = tk.Toplevel(ventanaMain)
    ventanaTorneo6.title("Torneo")
    anchoVentana = 850
    altoVentana = 450
    x = (ventanaTorneo6.winfo_screenwidth() - anchoVentana)//2
    y = (ventanaTorneo6.winfo_screenheight() - altoVentana)//2
    ventanaTorneo6.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
    #ventanaMain.withdraw()
    ventanaTorneo6.focus_force()
    ventanaTorneo6.grab_set()
    ventanaTorneo6.resizable(False, False)
    ventanaTorneo6.configure(bg="lightgray")
    ventanaTorneo6.bind("<Double-Button-1>", desseleccionarFila)

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

    botonTerminarTorneo = tk.Button(ventanaTorneo6, text="Terminar", font=15, command=lambda:ventanaTorneo6.destroy())
    botonTerminarTorneo.pack(padx=10, pady=10, side=tk.RIGHT)

    botonVerDatos = tk.Button(ventanaTorneo6, text="Datos", font=15, command=verDatos)
    botonVerDatos.pack(padx=10, pady=10, side=tk.RIGHT)