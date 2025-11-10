import sqlite3 as sql

#Jugadores ordenados por nombre
def consultarDatosJugadores(filtro=None):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        if filtro == "Nombre":
            instrucccion = "SELECT * FROM Jugadores ORDER BY [Nombre y Apellido] COLLATE NOCASE ASC"
        elif filtro == "Genero":
            instrucccion = "SELECT * FROM Jugadores ORDER BY Genero COLLATE NOCASE ASC"
        elif filtro == "Facultad":
            instrucccion = "SELECT * FROM Jugadores ORDER BY Facultad COLLATE NOCASE ASC"
        elif filtro == "Elo":
            instrucccion = "SELECT * FROM Jugadores ORDER BY Elo DESC"
        elif filtro == "Victorias":
            instrucccion = "SELECT * FROM Jugadores ORDER BY Victorias DESC"
        elif filtro == "Torneos":
            instrucccion = "SELECT * FROM Jugadores ORDER BY Torneos DESC"
        elif filtro == "Medallas":
            instrucccion = "SELECT * FROM Jugadores ORDER BY Medallas DESC"
        else:
            instrucccion = "SELECT [Nombre y Apellido], Facultad, Torneos, Medallas FROM Jugadores Where Medallas > 0 ORDER BY Medallas DESC, Torneos ASC"
            
        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        if resultados == None:
            return True
        
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosJugadores):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()
#Consultar datos de un jugador específico
def consultarDatosJugador(nombreTorneo, nombreJugador, antesTorneo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        if antesTorneo == True:
            instrucccion = f"SELECT [Nombre y Apellido], Genero, Facultad, Elo FROM Jugadores WHERE [Nombre y Apellido] == '{nombreJugador}'"
            cursor.execute(instrucccion)
            datosJugador = cursor.fetchall()
            datosJugador = list(datosJugador[0])
            if datosJugador == None:
                return False
            respuesta = agregarDatosAntesTorneo(nombreTorneo, list(datosJugador))
        else:
            instrucccion = f"SELECT [Nombre y Apellido], Genero, Facultad, Elo, Victorias, Medallas, Torneos FROM Jugadores WHERE [Nombre y Apellido] == '{nombreJugador}'"
            cursor.execute(instrucccion)
            datosJugador = cursor.fetchall()
            datosJugador = list(datosJugador[0])
            if datosJugador == None:
                return True
            respuesta = agregarDatosDespuesTorneo(nombreTorneo, list(datosJugador), antesTorneo)
        return respuesta
    except Exception as e:
        print("Error al consultar datos (consultarDatosJugador):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosAntesTorneo(nombreTorneo):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"SELECT name FROM sqlite_master WHERE type='table' AND name = '{nombreTorneo}'"
        cursor.execute(instrucccion)
        if cursor.fetchone() != None:
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
        instrucccion = f"SELECT * FROM '{nombreTorneo}' ORDER BY Puntos DESC, [Desempate (1)] DESC, [Desempate (2)] DESC"
        cursor.execute(instrucccion)
        jugadoresInscritos = cursor.fetchall()
        return jugadoresInscritos
    except Exception as e:
        print("Error al consultar datos (consultarDatosDespuesTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosListaTorneos(filtro):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        if filtro == "Nombre":
            instrucccion = "SELECT * FROM listaTorneos ORDER BY Nombre COLLATE NOCASE ASC"
        elif filtro == "Participantes":
            instrucccion = "SELECT * FROM listaTorneos ORDER BY Participantes DESC"
        elif filtro == "Rondas":
            instrucccion = "SELECT * FROM listaTorneos ORDER BY Rondas DESC"
        elif filtro == "Invitados":
            instrucccion = "SELECT * FROM listaTorneos ORDER BY Invitados COLLATE NOCASE DESC"
        elif filtro == "Descripcion":
            instrucccion = "SELECT * FROM listaTorneos ORDER BY Descripcion COLLATE NOCASE ASC"
        else:
            instrucccion = "SELECT * FROM listaTorneos ORDER BY Fecha COLLATE NOCASE DESC"

        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosListaTorneos):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosRanking(filtro):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        if filtro == "Femenino":
            instrucccion = "SELECT * FROM Jugadores WHERE Facultad != 'Invitado' AND Genero = 'F' ORDER BY Elo DESC, Victorias DESC, Medallas DESC"
        else:
            instrucccion = "SELECT * FROM Jugadores WHERE Facultad != 'Invitado' ORDER BY Elo DESC, Victorias DESC, Medallas DESC"
        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosRanking):", e)
    finally:
        conexion.commit()
        conexion.close()

def consultarDatosMedallas(filtro):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        if filtro == "Nombre":
            instrucccion = "SELECT * FROM Medallas ORDER BY [Nombre y Apellido] COLLATE NOCASE ASC"
        elif filtro == "Facultad":
            instrucccion = "SELECT * FROM Medallas ORDER BY Facultad COLLATE NOCASE ASC"
        elif filtro == "Torneos":
            instrucccion = "SELECT * FROM Medallas ORDER BY Torneos DESC"
        elif filtro == "Medallas":
            instrucccion = "SELECT * FROM Medallas ORDER BY Medallas DESC"
        elif filtro == "Oro":
            instrucccion = "SELECT * FROM Medallas ORDER BY Oro DESC"
        elif filtro == "Plata":
            instrucccion = "SELECT * FROM Medallas ORDER BY Plata DESC"
        elif filtro == "Bronce":
            instrucccion = "SELECT * FROM Medallas ORDER BY Bronce DESC"
        elif filtro == "Otra":
            instrucccion = "SELECT * FROM Medallas ORDER BY Otra DESC"
        elif filtro == "Estado":
            instrucccion = "SELECT * FROM Medallas ORDER BY Estado DESC"
        else:
            instrucccion = "SELECT * FROM Medallas ORDER BY Medallas DESC, Torneos ASC, Oro DESC, Plata DESC, Bronce DESC, Otra DESC"

        cursor.execute(instrucccion)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print("Error al consultar datos (consultarDatosMedallas):", e)
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
        nombreTorneo = f"AT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}"
        instrucccion = f"""CREATE TABLE '{nombreTorneo}'(
                                                    'Nombre y Apellido' TEXT,
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
        nombreTorneo = f"DT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}"
        instrucccion = f"""CREATE TABLE '{nombreTorneo}'(
                                                    'Nombre y Apellido' TEXT,
                                                    Genero TEXT DEFAULT 'M',
                                                    Facultad TEXT DEFAULT 'Ingeniería',
                                                    'Elo (+/-)' TEXT DEFAULT '0',
                                                    'Victorias (+)' TEXT DEFAULT '0',
                                                    'Medallas (+)' TEXT DEFAULT '0',
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
    finally:
        conexion.commit()
        conexion.close()

def crearTablaJugadores():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"""CREATE TABLE IF NOT EXISTS Jugadores (
                                                                'Nombre y Apellido'	TEXT,
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
                                                                Nombre TEXT,
                                                                Fecha TEXT DEFAULT '00))/00/00',
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

def crearTablaMedallas():
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"""CREATE TABLE IF NOT EXISTS Medallas (
                                                                'Nombre y Apellido'	TEXT,
                                                                Facultad TEXT DEFAULT 'Ingeniería',
                                                                Torneos	INTEGER DEFAULT 0,
                                                                Medallas INTEGER DEFAULT 0,
                                                                Oro INTEGER DEFAULT 0,
                                                                Plata INTEGER DEFAULT 0,
                                                                Bronce INTEGER DEFAULT 0,
                                                                Otra INTEGER DEFAULT 0,
                                                                Estado TEXT DEFAUL '✖',
                                                                PRIMARY KEY('Nombre y Apellido')
                                                                )"""
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al crear (crearTablaMedallas):", e)
    finally:
        conexion.commit()
        conexion.close()        

def agregarDatosJugadores(*datosJugador):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"INSERT INTO Jugadores VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instrucccion, (datosJugador))
        return datosJugador[0]
    except Exception as e:
        print("Error al agregar datos (agregarDatosJugadores):", e)
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

def agregarDatosMedallas(datosJugador):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion =f"INSERT OR IGNORE INTO Medallas ([Nombre y Apellido], Facultad, Torneos, Medallas) VALUES(?, ?, ?, ?)"
        cursor.execute(instrucccion, datosJugador)
    except Exception as e:
        print("Error al agregar datos (agregarDatosMedallas):", e)
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
        instrucccion = f"UPDATE Medallas SET [Nombre y Apellido] = '{nombreCompleto}', Facultad = '{facultad}',  Torneos = {torneos}, Medallas = {medallas} Where [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
        return nombreJugador
    except Exception as e:
        print("Error al actualizar datos (actualizarDatosJugador):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def editarTablaAntesTorneo(nombreViejo, nombre, fecha, participantes, rondas, invitados, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreNuevo = f"AT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}".replace("-", "/")
        instrucccion = f"ALTER TABLE '{nombreViejo}' RENAME TO '{nombreNuevo}'"
        cursor.execute(instrucccion)
        return nombreNuevo
    except Exception as e:
        print("Error al agregar datos (editarTablaAntesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def editarTablaDespuesTorneo(nombreViejo, nombre, fecha, participantes, rondas, invitados, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        nombreNuevo = f"DT_{nombre}_{fecha}_P{participantes}_R{rondas}_{invitados}{"_" if descripcion != "" else ""}{descripcion}".replace("-", "/")
        instrucccion = f"ALTER TABLE '{nombreViejo}' RENAME TO '{nombreNuevo}'"
        cursor.execute(instrucccion)
        return nombreNuevo
    except Exception as e:
        print("Error al agregar datos (editarTablaDespuesTorneo:", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def actualizarDatosJugador(nombreJugador, facultad, elo, victorias, torneos, medallas, tipoMedalla=None):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instruccion = f"UPDATE Jugadores SET Elo = {elo}, Victorias = {victorias}, Torneos = {torneos}, Medallas = {medallas} WHERE [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instruccion)
        instruccion = f"INSERT OR IGNORE INTO Medallas ([Nombre y Apellido], Facultad, Torneos, Medallas) VALUES(?, ?, ?, ?)"
        cursor.execute(instruccion, (nombreJugador, facultad, torneos, medallas))
        if tipoMedalla != None:
            instruccion = f"UPDATE Medallas SET Torneos = {torneos}, Medallas = {medallas}, {tipoMedalla} = {tipoMedalla}+1 WHERE [Nombre y Apellido] = '{nombreJugador}'"
            cursor.execute(instruccion)

        return nombreJugador
    except Exception as e:
        print("Error al actualizar datos (actualizarDatosJugador):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def actualizarMedallasJugador(nombreJugador, medallas, oro, plata, bronce, otra):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"UPDATE Medallas SET Medallas = {medallas}, Oro = {oro}, Plata = {plata}, Bronce = {bronce}, Otra = {otra}, Estado = '✔' Where [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
        instrucccion = f"UPDATE Jugadores SET Medallas = {medallas} WHERE [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al actualizar datos (actualizarMedallasJugador):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()  

def actualizarTablaDespuesTorneo(nombreTorneo, nombreJugador, elo, victorias, medallas):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"UPDATE '{nombreTorneo}' SET [Elo (+/-)] = '{elo}', [Victorias (+)] = '{victorias}', [Medallas (+)] = '{medallas}' Where [Nombre y Apellido] = '{nombreJugador}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al actualizar datos (actualizarTablaDespuesTorneo):", e)
        return True
    finally:
        conexion.commit()
        conexion.close()

def editarTablaListaTorneo(nombreTorneo, nombre, fecha, descripcion):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"UPDATE listaTorneos SET Nombre = '{nombre}', Fecha = '{fecha}', Descripcion = '{descripcion}' Where Nombre = '{nombreTorneo}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al actualizar datos (editarTablaListaTorneo):", e)
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
        instrucccion = f"DELETE FROM Medallas WHERE [Nombre y Apellido] = '{nombreCompleto}'"
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
        instrucccion = f"DROP TABLE IF EXISTS '{nombreTorneo}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al eliminar datos (eliminarTabla):", e)
    finally:
        conexion.commit()
        conexion.close()

def eliminarJugadorMedallas(nombreCompleto):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"DELETE FROM Medallas WHERE [Nombre y Apellido] = '{nombreCompleto}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al eliminar datos (eliminarJugadorMedallas):", e)
    finally:
        conexion.commit()
        conexion.close()

def eliminarTorneo(nombre, nombreTorneos):
    try:
        conexion = sql.connect("ajedrez.db")
        cursor = conexion.cursor()
        instrucccion = f"DELETE FROM listaTorneos WHERE Nombre = '{nombre}'"
        cursor.execute(instrucccion)
        instrucccion = f"DROP TABLE IF EXISTS '{"AT_"+nombreTorneos}'"
        cursor.execute(instrucccion)
        instrucccion = f"DROP TABLE IF EXISTS '{"DT_"+nombreTorneos}'"
        cursor.execute(instrucccion)
    except Exception as e:
        print("Error al eliminar datos (eliminarTorneo):", e)
    finally:
        conexion.commit()
        conexion.close()

