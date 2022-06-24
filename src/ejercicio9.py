#############
# Yonathan Ignacio Opazo Almonacid - yonaopazo_github
# UNR Andina - Introducio a la Ingenieria en Computacion
#############
"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
def factores_primos(numero):
    for numero in range(1,100):
        if numero > 1:
            cont=0
            i=2
            while i<numero and cont==0:
                resto=numero%i
                if resto==0:
                    cont+=1
                i+=1
            if cont==0:
                return True
            else:
                return False
        else:
            return False
        
def principal():
    #esta funion es la encargada de la parte "interactiva" del ejercicio(la entrada, la llamada al algoritmo y la salida.)

if __name__ == "__main__":
    principal()
