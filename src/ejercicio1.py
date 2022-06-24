#############
# Yonathan Ignacio Opazo Almonacid - yonaopazo_github
# UNR Andina - Introducio a la Ingenieria en Computacion
#############
"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrenheit(centigrados):
    """
    funcion encargada de convertir grados fahrenheit a centigrados.
    retorna el resultado de la ecuacion en un numero float.
    """
    ec_fahrenheit = (centigrados*1.8)+32
    return ec_fahrenheit

def convertir_a_centigrados(fahrenheit):
    """
    funcion encargada de convertir grados de centigrados a fahrenheit.
    retorna el resultado de la ecuacion en un numero float.
    """
    ec_centigrados = (fahrenheit - 32)*5/9
    return ec_centigrados

print(convertir_a_fahrenheit(-50))
    


    
