import sqlite3 as sql

#Jugadores ordenados por nombre
def consultarDatosJugadores(filtro=None):
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
def consultarDatosJugador(nombreTorneo, nombreJugador, antesTorneo):
    try:
        #print("Consultando datos de jugador:", nombreJugador)
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        if antesTorneo == True:
            instrucccion = f"SELECT [Nombre y Apellido], Genero, Facultad, Elo FROM Jugadores WHERE [Nombre y Apellido] == '{nombreJugador}'"
            cursor.execute(instrucccion)
            datosJugador = cursor.fetchall()
            datosJugador = list(datosJugador[0])
            respuesta = agregarDatosAntesTorneo(nombreTorneo, list(datosJugador))
        else:
            instrucccion = f"SELECT [Nombre y Apellido], Genero, Facultad, Elo, Victorias, Medallas, Torneos FROM Jugadores WHERE [Nombre y Apellido] == '{nombreJugador}'"
            cursor.execute(instrucccion)
            datosJugador = cursor.fetchall()
            datosJugador = list(datosJugador[0])
            respuesta = agregarDatosDespuesTorneo(nombreTorneo, list(datosJugador), antesTorneo)
        return respuesta
    except Exception as e:
        print("Error al consultar datos (consultarDatosJugador):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosAntesTorneo(nombreTorneo):
    try:
        #print("Consultando datos del torneo:", nombreTorneo)
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"SELECT * FROM '{nombreTorneo}' ORDER BY Elo DESC"
        cursor.execute(instrucccion)
        jugadoresInscritos = cursor.fetchall()
        return jugadoresInscritos
    except Exception as e:
        print("Error al consultar datos (consultarDatosAntesTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosDespuesTorneo(nombreTorneo):
    try:
        #print("Consultando datos del torneo:", nombreTorneo)
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"SELECT * FROM '{nombreTorneo}'ORDER BY Puntos DESC, [Desempate (1)] DESC, [Desempate (2)] DESC"
        cursor.execute(instrucccion)
        jugadoresInscritos = cursor.fetchall()
        return jugadoresInscritos
    except Exception as e:
        print("Error al consultar datos (consultarDatosDespuesTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosListaTorneos():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = "SELECT * FROM listaTorneos ORDER BY Nombre COLLATE NOCASE ASC"
        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosListaTorneos):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosRanking(filtro=None):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = "SELECT * FROM Jugadores ORDER BY Elo DESC, Victorias DESC, Medallas DESC"
        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosRanking):", e)
    finally:
        conexion.commit()
        conexion.close()
        
def eliminarJugadorTorneo(nombre, apellido, medallas, torneos):
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
        nombreTorneo = f"AT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}".replace("-", "/")
        instrucccion = f"""CREATE TABLE '{nombreTorneo}'(
                                                    'Nombre y Apellido' TEXT Default 'Nombre',
                                                    Genero TEXT DEFAULT 'M',
                                                    Facultad TEXT DEFAULT 'Ingeniería',
                                                    Elo INTEGER DEFAULT 1500,
                                                    Victorias TEXT DEFAULT '0',
                                                    Tablas TEXT DEFAULT '0',
                                                    Derrotas TEXT DEFAULT '0',
                                                    Puntos NUMERIC DEFAULT 0,
                                                    'Desempate (1)' REAL DEFAULT 0.00,
                                                    'Desempate (2)' REAL DEFAULT 0.00,
                                                    'Diferencia Elo' INTEGER DEFAULT 0,
                                                    PRIMARY KEY('Nombre y Apellido')
                                                    )"""
        cursor.execute(instrucccion)
        return nombreTorneo
    except Exception as e:
        print("Error al agregar datos (crearTablaAntesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()
        
def crearTablaDespuesTorneo(nombre, fecha, participantes, rondas, invitados, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreTorneo = f"DT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}".replace("-", "/")
        instrucccion = f"""CREATE TABLE '{nombreTorneo}'(
                                                    'Nombre y Apellido' TEXT DEFAULT 'Nombre',
                                                    Genero TEXT DEFAULT 'M',
                                                    Facultad TEXT DEFAULT 'Ingeniería',
                                                    'Elo (+/-)' INTEGER DEFAULT 1500,
                                                    'Victorias (+)' INTEGER DEFAULT 0,
                                                    'Medallas (+)' INTEGER DEFAULT 0,
                                                    Torneos	INTEGER DEFAULT 0,
                                                    Puntos NUMERIC DEFAULT 0,
                                                    'Desempate (1)'	REAL DEFAULT 0.00,
                                                    'Desempate (2)'	REAL DEFAULT 0.00,
                                                    PRIMARY KEY('Nombre y Apellido')
                                                    )"""
        cursor.execute(instrucccion)
        return nombreTorneo
    except Exception as e:
        print("Error al agregar datos (crearTablaDespuesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def crearTablaJugadores():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"""CREATE TABLE IF NOT EXISTS Jugadores (
                                                                'Nombre y Apellido'	TEXT DEFAULT 'Nombre',
                                                                Genero	TEXT DEFAULT 'M',
                                                                Facultad TEXT DEFAULT 'Ingeniería',
                                                                Elo	INTEGER DEFAULT 1500,
                                                                Victorias INTEGER DEFAULT 0,
                                                                Torneos	INTEGER DEFAULT 0,
                                                                Medallas INTEGER DEFAULT 0,
                                                                PRIMARY KEY('Nombre y Apellido')
                                                                )"""
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al crear (crearTablaJugadores):", e)
    finally:
        conexion.commit()
        conexion.close()

def crearTablaListaTorneos():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"""CREATE TABLE IF NOT EXISTS listaTorneos (
                                                                Nombre TEXT DEFAULT 'Torneo',
                                                                Fecha TEXT DEFAULT '00/00/00',
                                                                Participantes INTEGER DEFAULT 0,
                                                                Rondas INTEGER DEFAULT 0,
                                                                Invitados TEXT DEFAULT 'False',
                                                                Descripcion	TEXT DEFAULT 'Ninguna',
                                                                PRIMARY KEY('Nombre')
                                                                )"""
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al crear (crearTablaListaTorteos):", e)
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosJugadores(*datosJugador):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Jugadores VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instrucccion, (datosJugador))
        return datosJugador[1]
    except Exception as e:
        print("Error al agregar datos (agregarDatosJugadore):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosAntesTorneo(nombreTorneo, datosJugador):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO'{nombreTorneo}'([Nombre y Apellido], Genero, Facultad, Elo) VALUES(?, ?, ?, ?)"
        cursor.execute(instrucccion, (datosJugador))
    except Exception as e:
        print("Error al agregar datos (agregarDatosAntesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosDespuesTorneo(nombreTorneo, datos, desempate):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO'{nombreTorneo}' ([Nombre y Apellido], Genero, Facultad, [Elo (+/-)], [Victorias (+)], [Medallas (+)], Torneos, Puntos, [Desempate (1)], [Desempate (2)]) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        datosJugador = list(datos) + list(desempate)
        cursor.execute(instrucccion, (datosJugador))
        #print(datosJugador)
    except Exception as e:
        print("Error al agregar datos (agregarDatosDespuesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def agregarDatosListaTorneos(*datosTorneo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO listaTorneos VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(instrucccion, datosTorneo)
    except Exception as e:
        print("Error al agregar datos (agregarDatosListaTorneos):", e)
    finally:
        conexion.commit()
        conexion.close()

def actualizarJugadorTorneo(nombreTorneo, nombreJugador, victorias, tablas, derrotas, puntos, desempate1, desempate2, diferenciaElo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"UPDATE '{nombreTorneo}'SET Victorias = '{victorias}', Tablas = '{tablas}', Derrotas = '{derrotas}', Puntos = {puntos}, [Desempate (1)] = {desempate1}, [Desempate (2)] = {desempate2}, [Diferencia Elo] = {diferenciaElo} Where [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
        return nombreJugador
    except Exception as e:
        print("Error al actualizar datos (actualizarJugadorTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def editarDatosJugador(nombreJugador, nombreCompleto, genero, facultad, elo, victorias, torneos, medallas):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"UPDATE Jugadores SET [Nombre y Apellido] = '{nombreCompleto}', Genero = '{genero}', Facultad = '{facultad}', Elo = {elo}, Victorias = {victorias}, Torneos = {torneos}, Medallas = {medallas} Where [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
        return nombreJugador
    except Exception as e:
        print("Error al actualizar datos (actualizarDatosJugador):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def actualizarAntesTorneo(nombreViejo, nombre, fecha, participantes, rondas, invitados, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreNuevo = f"AT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}".replace("-", "/")
        instrucccion = f"ALTER TABLE '{nombreViejo}' RENAME TO '{nombreNuevo}'"
        cursor.execute(instrucccion)
        return nombreNuevo
    except Exception as e:
        print("Error al agregar datos (actualizarAntesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def actualizarDatosJugador(nombreJugador, elo, victorias, torneos, medallas):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"UPDATE Jugadores SET Elo = {elo}, Victorias = {victorias}, Torneos = {torneos}, Medallas = {medallas} Where [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
        return nombreJugador
    except Exception as e:
        print("Error al actualizar datos (actualizarDatosJugador):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def eliminarJugadorTorneo(nombreTorneo, nombreCompleto):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"DELETE FROM '{nombreTorneo}' WHERE [Nombre y Apellido] = '{nombreCompleto}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al eliminar datos (eliminarJugadorTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

def eliminarDatosJugador(nombreCompleto):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"DELETE FROM Jugadores WHERE [Nombre y Apellido] = '{nombreCompleto}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al eliminar datos (eliminarDatosJugador):", e)
    finally:
        conexion.commit()
        conexion.close()

def eliminarTabla(nombreTorneo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"DROP TABLE '{nombreTorneo}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al eliminar datos (eliminarTabla):", e)
    finally:
        conexion.commit()
        conexion.close()


