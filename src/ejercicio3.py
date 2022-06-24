#############
# Yonathan Ignacio Opazo Almonacid - yonaopazo_github
# UNR Andina - Introducio a la Ingenieria en Computacion
#############
"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
def compara(numero, otro_numero):
    if numero < otro_numero:
        retorna = -1
    elif numero > otro_numero:
        retorna = 1
    else:
        retorna = 0
    return retorna

def principal():
    #esta funion es la encargada de la parte "interactiva" del ejercicio(la entrada, la llamada al algoritmo y la salida.)

if __name__ == "__main__":
    principal()
        
