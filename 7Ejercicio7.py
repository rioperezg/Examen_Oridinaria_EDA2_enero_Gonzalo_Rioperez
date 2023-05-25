"""
Ash Ketchum, líder del equipo de entrenadores Pokemon, tiene dificultades para transmitir los mensajes al Centro Pokemon, 
dado que los mismos son muy largos y los satélites espías del Equipo Rocket los interceptan, en un lapso muy corto desde que se 
transmiten. Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los mensajes para enviarlos más rápido y no 
puedan ser interceptados. Contemplando los siguientes requerimientos, implementar un algoritmo que pueda crear un árbol de Huffman a 
partir de la siguiente tabla y desarrollar las funciones para comprimir y descomprimir un mensaje.
"""
class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor
class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class Caracter(object):
    def __init__(self):
        size = int(input("Cuantas letras tiene la tabla en total?: "))
        self.string = input("Caracter: ")
        self.cantidad = int(input("Cantidad: "))
        self.frecuencia = self.cantidad / size
raiz = None
letra = Caracter()
while(letra.string != ""):
    
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
