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
    if texto.strip() == "":
        return False
    elif len(texto) > 15:
        return False
    return True
