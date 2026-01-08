def validarNombre(nombre):
    if len(nombre) > 20:
        return False
    if nombre.strip() == "":
            return False
    for letra in nombre:
        if letra == " ":
            continue 
        if not letra.isalnum():
            return False
    return True

def validarEntero(entero):
    if entero.strip() == "":
        return False
    for i in entero:
        if not i.isnumeric():
            return False
    return True
        
def validarTexto(texto):
    if len(texto) > 20:
        return False
    return True

def validarFloat(numero):
    try:
        numero = float(numero)
        return True
    except ValueError:
        return False
    
def validarEntero2(numero):
    try:
        numero = int(numero)
        return str(numero)
    except ValueError:
        return 0
    
def validarEloVictorias(victorias):
    diferencia = 0
    if victorias.strip() == "":
        return 0
    for i in victorias:
        if i == "+":
            diferencia += 8
        elif i == "-":
            diferencia += 2
        elif i == "=":
            diferencia += 4
        elif i == "B":
            diferencia += 0
        elif i == "F":
            diferencia += 0
        else:
            return "False"
    return diferencia
        
def validarEloTablas(tablas):
    diferencia = 0
    if tablas.strip() == "":
        return 0
    for i in tablas:
        if i == "+":
            diferencia += 2
        elif i == "-":
            diferencia -= 2
        elif i == "=":
            diferencia = 0
        else:
            return "False"
    return diferencia

def validarEloDerrotas(derrotas):
    diferencia = 0
    if derrotas.strip() == "":
        return 0
    for i in derrotas:
        if i == "+":
            diferencia -= 8
        elif i == "-":
            diferencia -= 2
        elif i == "=":
            diferencia -= 4
        elif i == "B":
            diferencia += 0
        elif i == "F":
            diferencia += 0
        else:
            return "False"
    return diferencia

def validarDiferenciaVictorias(diferencia, respuesta):
    if respuesta == "Bye":
        return "Bye(B)"
    elif respuesta == "Forfeit":
        return "Forfeit(+F)"
    
    if  diferencia <= -100:
        return f"{respuesta[0][0]} {respuesta[0][3]} (V+)"
    elif diferencia >= 100:
        return f"{respuesta[0][0]} {respuesta[0][3]} (V-)"
    else:
        return f"{respuesta[0][0]} {respuesta[0][3]} (V=)"

def validarDiferenciaTablas(diferencia, respuesta):
    if  diferencia < 0:
        return f"{respuesta[0][0]} {respuesta[0][3]} (T+)"
    elif diferencia > 0:
        return f"{respuesta[0][0]} {respuesta[0][3]} (T-)"
    else:
        return f"{respuesta[0][0]} {respuesta[0][3]} (T=)"
    
def validarDiferenciaDerrotas(diferencia, respuesta):
    if respuesta == "Bye":
        return "Bye(B)"
    elif respuesta == "Forfeit":
        return "Forfeit(-F)"
    
    if  diferencia >= 100:
        return f"{respuesta[0][0]} {respuesta[0][3]} (D+)"
    elif diferencia <= -100:
        return f"{respuesta[0][0]} {respuesta[0][3]} (D-)"
    else:
        return f"{respuesta[0][0]} {respuesta[0][3]} (D=)"
