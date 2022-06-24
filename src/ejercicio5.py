#############
# Yonathan Ignacio Opazo Almonacid - yonaopazo_github
# UNR Andina - Introducio a la Ingenieria en Computacion
#############
"""
5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""
def division_lenta(dividendo, divisor):
    if dividendo and divisor >= 0:
        cociente = 0
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            cociente = cociente + 1
        resto = dividendo
        return resto, cociente
    
def principal():
    #esta funion es la encargada de la parte "interactiva" del ejercicio(la entrada, la llamada al algoritmo y la salida.)

if __name__ == "__main__":
    principal()