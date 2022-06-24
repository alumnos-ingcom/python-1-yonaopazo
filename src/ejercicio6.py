#############
# Yonathan Ignacio Opazo Almonacid - yonaopazo_github
# UNR Andina - Introducio a la Ingenieria en Computacion
#############
"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""
def ordenar_mayor_a_menor(uno,dos,tres):
    if uno > dos and uno > tres:
        if dos > tres: 
            tupla = (uno,dos,tres)
        else:
            tupla = (uno,tres,dos)
    elif dos > uno and dos > tres:
        if uno > tres:
            tupla= (dos,uno,tres)
        else:
            tupla=(dos,tres,uno)
    else:
        if uno > dos:
            tupla = (tres,uno,dos)
        else:
            tupla = (tres,dos,uno)    
    return tupla
    

def ordenar_menor_a_mayor(uno,dos,tres):
    if uno > dos and uno > tres:
        if dos > tres: 
            tupla = (uno,dos,tres)
        else:
            tupla = (uno,tres,dos)
    elif dos > uno and dos > tres:
        if uno > tres:
            tupla= (dos,uno,tres)
        else:
            tupla=(dos,tres,uno)
    else:
        if uno > dos:
            tupla = (tres,uno,dos)
        else:
            tupla = (tres,dos,uno)
            newtupla = (tuple(reversed(tupla)))
            
    return newtupla

def principal():
    #esta funion es la encargada de la parte "interactiva" del ejercicio(la entrada, la llamada al algoritmo y la salida.)

if __name__ == "__main__":
    principal()