import sqlite3 as sql

def consultarDatosJugadores():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = "SELECT * FROM Jugadores"
        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (Jugadores):", e)
    finally:
        conexion.close()

def agregarDatosJugadores(nombreCompleto, género, facultad, elo, victorias, torneos, invitado):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Jugadores VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instrucccion, (nombreCompleto, género, facultad, elo, victorias, torneos, invitado))
        conexion.commit()
        return nombreCompleto
    except Exception as e:
        print("Error al agregar datos (Jugadores):", e)
        return True
    finally:
        conexion.close()
        
def agregarDatosMedallas(nombre, apellido, medallas, torneos):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Medallas VALUES('{nombre}', '{apellido}', {medallas}, {torneos})"
        cursor.execute(instrucccion)
        conexion.commit()
    except Exception as e:
        print("Error al agregar datos (Medallas):", e)
    finally:
        conexion.close()

def crearTablaAntesTorneo(nombre, fecha, participantes, rondas, invitados, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreTorneo = f"{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}_{descripcion}".replace("-", "/")
        instrucccion = f"""CREATE TABLE '{nombreTorneo}'(
                                                    Nombre TEXT,
                                                    Apellido TEXT,
                                                    Elo INTEGER,
                                                    Victorias INTEGER,
                                                    Tablas INTEGER,
                                                    Derrotas INTEGER,
                                                    Puntos REAL,
                                                    'Desempate (1)' REAL,
                                                    'Desempate (2)' REAL
                                                    )"""
        cursor.execute(instrucccion)
        conexion.commit()
        return nombreTorneo
    except Exception as e:
        print("Error al agregar datos (crearTablaAntesTorneo):", e)
        return True
    finally:
        conexion.close()

def agregarDatosAntesTorneo(nombre, apellido, elo, victorias, tablas, derrotas, puntos, desempate1, desempate2):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO antesTorneo VALUES(?,?,?,?,?,?,?,?,?)"
        cursor.execute(instrucccion, (nombre, apellido, elo, victorias, tablas, derrotas, puntos, desempate1, desempate2))
        conexion.commit()
    except Exception as e:
        print("Error al agregar datos (agregarDatos):", e)
    finally:
        conexion.close()

def agregarDatosRankingGeneral(nombre, apellido, facultad, victorias, elo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO rankingGeneral VALUES('{nombre}', '{apellido}', '{facultad}', {victorias}, {elo})"
        cursor.execute(instrucccion)
        conexion.commit()
    except Exception as e:
        print("Error al agregar datos (agregarDatosRankingGeneral):", e)
    finally:
        conexion.close()


