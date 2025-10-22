def validarNombre(nombre):
    for i in nombre:
        if not i.isalpha():
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