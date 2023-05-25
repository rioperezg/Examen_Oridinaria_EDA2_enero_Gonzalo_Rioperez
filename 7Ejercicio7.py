"""
Ash Ketchum, líder del equipo de entrenadores Pokemon, tiene dificultades para transmitir los mensajes al Centro Pokemon, 
dado que los mismos son muy largos y los satélites espías del Equipo Rocket los interceptan, en un lapso muy corto desde que se 
transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los mensajes para enviarlos más rápido y no 
puedan ser interceptados. Contemplando los siguientes requerimientos, implementar un algoritmo que pueda crear un árbol de Huffman a 
partir de la siguiente tabla y desarrollar las funciones para comprimir y descomprimir un mensaje.
"""
class nodoArbolHuffman(object):
    
    def __init__(self, info, frecuencia):
        self.izq = None
        self.der = None
        self.info = int(input("(Pulse enter si quiere salir)Ingrese el caracter: "))
        self.frecuencia = float(input("Pulse enter si quiere salir)Ingrese la frecuencia: "))

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
    def insertar_nodo(raiz, dato, frecuencia):
        if(raiz is None):
            raiz = nodoArbolHuffman(dato, frecuencia)
        elif(dato < raiz.info):
            raiz.izq = nodoArbolHuffman.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbolHuffman.insertar_nodo(raiz.der, dato)
            return raiz
        
Raiz = None
i = int(input("Cuantas letras va a ingresar: "))
while(i != 0):
    raiz = nodoArbol.insertar_nodo(raiz=Raiz)



    
    # Hay q almacenar primeramente los caracteres en una lista segun peso y orden alfabetico




# Estas dos funciones las necesitaremos seguro
def generar_tabla(nodo, tabla, codigo=""):
    if nodo is not None:
        if nodo.izquierdo is None and nodo.derecho is None:
            tabla[nodo.caracter] = codigo
        else:
            generar_tabla(nodo.izquierdo, tabla, codigo + "0")
            generar_tabla(nodo.derecho, tabla, codigo + "1")
 
def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izquierdo
        else:
            raiz_aux = raiz_aux.derecho
        pos += 1
        if(raiz_aux.izquierdo is None):
            cadena_deco += raiz_aux.caracter
            raiz_aux = arbol_huff
    return cadena_deco
