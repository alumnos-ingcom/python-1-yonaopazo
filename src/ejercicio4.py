"""
4. Suma lenta
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
def suma_lenta(numero, otro_numero):
    suma = numero + otro_numero
    if numero and otro_numero >= 0:
        print(numero, end="")
        while numero < suma:
            numero=numero + 1
            print("+1",end='')
        print(f" = {numero}")    
    if numero and otro_numero <= 0:
        print(numero, end="")
        while numero > suma:
            numero = numero - 1    
            print("-1",end='')
        print(f" = {numero}")
        
def principal():
    #esta funion es la encargada de la parte "interactiva" del ejercicio(la entrada, la llamada al algoritmo y la salida.)

if __name__ == "__main__":
    principal()
    
    