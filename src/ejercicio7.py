"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    if horas >= 0 and minutos >=0 and segundos >=0:
        horas = horas * 60 * 60
        minutos = minutos * 60
        segundos = horas + minutos + segundos
        tuple = (segundos)
        return tuple
    
def decimal_a_sexadecimal(segundos):
    if segundos >= 0:
        horas = segundos // 3600
        minutos = (segundos - horas * 3600) // 60
        segundos = (segundos - horas * 3600 - minutos * 60)
        tuple = (horas,minutos,segundos)
        return tuple


def principal():
    #esta funion es la encargada de la parte "interactiva" del ejercicio(la entrada, la llamada al algoritmo y la salida.)

if __name__ == "__main__":
    principal()