import sqlite3 as sql

#Jugadores ordenados por nombre
def consultarDatosJugadores():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = "SELECT * FROM Jugadores ORDER BY [Nombre y Apellido] COLLATE NOCASE ASC"
        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosJugadores):", e)
    finally:
        conexion.commit()
        conexion.close()
#Consultar datos de un jugador específico
def consultarDatosJugador(nombreJugador, nombreTorneo):
    try:
        print("Consultando datos de jugador:", nombreJugador)
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"SELECT [Nombre y Apellido], Genero, Facultad, Elo FROM Jugadores WHERE [Nombre y Apellido] == '{nombreJugador}'"
        cursor.execute(instrucccion)
        datosJugador = cursor.fetchall()
        datosJugador = list(datosJugador[0])
        agregarDatosAntesTorneo(list(datosJugador), nombreTorneo)
    except Exception as e:
        print("Error al consultar datos (consultarDatosJugador):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosTorneo(nombreTorneo):
    try:
        print("Consultando datos del torneo:", nombreTorneo)
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"SELECT * FROM '{nombreTorneo}'"
        cursor.execute(instrucccion)
        jugadoresInscritos = cursor.fetchall()
        return jugadoresInscritos
    except Exception as e:
        print("Error al consultar datos (consultarDatosTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosJugadores(*args):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Jugadores VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instrucccion, (args))
        return args[1]
    except Exception as e:
        print("Error al agregar datos (agregarDatosJugadore):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()
        
def agregarDatosMedallas(nombre, apellido, medallas, torneos):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Medallas VALUES('{nombre}', '{apellido}', {medallas}, {torneos})"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al agregar datos (agregarDatosMedallas):", e)
    finally:
        conexion.commit()
        conexion.close()

def crearTablaAntesTorneo(nombre, fecha, participantes, rondas, invitados, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreTorneo = f"{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}_{descripcion}".replace("-", "/")
        instrucccion = f"""CREATE TABLE '{nombreTorneo}'(
                                                    'Nombre y Apellido' TEXT,
                                                    Genero TEXT,
                                                    Facultad TEXT,
                                                    Elo INTEGER,
                                                    Victorias INTEGER DEFAULT 0,
                                                    Tablas INTEGER DEFAULT 0,
                                                    Derrotas INTEGER DEFAULT 0,
                                                    Puntos REAL DEFAULT 0.0,
                                                    'Desempate (1)' REAL DEFAULT 0.00,
                                                    'Desempate (2)' REAL DEFAULT 0.00
                                                    )"""
        cursor.execute(instrucccion)
        return nombreTorneo
    except Exception as e:
        print("Error al agregar datos (crearTablaAntesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosAntesTorneo(datosJugador, nombreTorneo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO'{nombreTorneo}'([Nombre y Apellido], Genero, Facultad, Elo) VALUES(?, ?, ?, ?)"
        cursor.execute(instrucccion, (datosJugador))
    except Exception as e:
        print("Error al agregar datos (agregarDatosAntesTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosRankingGeneral(nombre, apellido, facultad, victorias, elo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO rankingGeneral VALUES('{nombre}', '{apellido}', '{facultad}', {victorias}, {elo})"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al agregar datos (agregarDatosRankingGeneral):", e)
    finally:
        conexion.commit()
        conexion.close()


