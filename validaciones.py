def validacion(msj='\nINGRESA LA CANTIDAD DE PARTICIPANTES EN LA COMPETENCIA: ', sup=16):
    x = int(input(msj))
    while x < sup or x > sup:
        print("ERRORR!!! ingrese correctamente la cantidad de participantes:  ")
        x = int(input(msj))
    return x


def validar_entre(inf, sup, msj):
    x = int(input(msj))
    if x not in range(inf, sup):
        print("ERRORR!!! porfavor vuelve a ingresar el numero .")
        x = int(input(msj))
    return x
