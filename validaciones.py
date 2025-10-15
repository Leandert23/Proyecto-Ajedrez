def validarNombre(nombre):
    for i in nombre:
        if not i.isalpha():
            return False
        return True

def validarParticipantes(participantes):
    for i in participantes:
        if not i.isnumeric():
            return False
    return True
        
def validarDescripcion(descripcion):
    if len(descripcion) > 15:
        return False
    return True
    
