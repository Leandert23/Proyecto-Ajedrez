import sqlite3 as sql

def agregarDatosJugadores(nombre, apellido, género, facultad, elo, invitado, torneos):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Jugadores VALUES('{nombre}', '{apellido}', '{género}', '{facultad}', {elo}, '{invitado}', {torneos})"
        cursor.execute(instrucccion)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error al agregar datos (Jugadores):", e)

def agregarDatosMedallas(nombre, apellido, medallas, torneos):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Medallas VALUES('{nombre}', '{apellido}', {medallas}, {torneos})"
        cursor.execute(instrucccion)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error al agregar datos (Medallas):", e)

def crearTablaAntesTorneo(nombre, fecha):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreTorneo = f"{nombre}_{fecha}".replace(" ", "")
        print(nombreTorneo)
        instrucccion = f"""CREATE TABLE {nombreTorneo}(
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
        conexion.close()
    except Exception as e:
        print("Error al agregar datos (crearTablaAntesTorneo):", e)

def agregarDatosAntesTorneo(nombre, apellido, elo, victorias, tablas, derrotas, puntos, desempate1, desempate2):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()  #Nombre de torneo
        instrucccion = f"INSERT INTO antesTorneo VALUES('{nombre}', '{apellido}', {elo}, {victorias}, {tablas}, {derrotas}, {puntos}, {desempate1}, {desempate2})"
        cursor.execute(instrucccion)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error al agregar datos (agregarDatos):", e)

def agregarDatosRankingGeneral(nombre, apellido, facultad, victorias, elo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO rankingGeneral VALUES('{nombre}', '{apellido}', '{facultad}', {victorias}, {elo})"
        cursor.execute(instrucccion)
        conexion.commit()
        conexion.close()
    except Exception as e:
        print("Error al agregar datos (agregarDatosRankingGeneral):", e)

