def validarNombre(nombre):
    if len(nombre) > 15:
        return False
    if nombre.strip() == "":
            return False
    for letra in nombre:
        if letra == " ":
            continue 
        if not letra.isalpha():
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
    if len(texto) > 15:
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
        return "False"
    if  victorias == "0":
        return 0
    for i in victorias:
        if i == "+":
            diferencia += 8
        elif i == "-":
            diferencia += 2
        elif i == "=":
            diferencia += 4
        else:
            return "False"
    return diferencia
        
def validarEloTablas(tablas):
    diferencia = 0
    if tablas.strip() == "":
        return "False"
    if  tablas == "0":
        return 0
    for i in tablas:
        if i == "+":
            diferencia += 2
        elif i == "-":
            diferencia -= 2
        else:
            return "False"
    return diferencia

def validarEloDerrotas(derrotas):
    diferencia = 0
    if derrotas.strip() == "":
        return "False"
    if  derrotas == "0":
        return 0
    for i in derrotas:
        if i == "+":
            diferencia -= 8
        elif i == "-":
            diferencia -= 2
        elif i == "=":
            diferencia -= 4
        else:
            return "False"
    return diferencia