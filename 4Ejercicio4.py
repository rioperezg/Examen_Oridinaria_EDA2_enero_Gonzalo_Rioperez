"""

Problema de los movimientos de un Abra en una red de Pokémon

Si se parte de la ruta 1, Abra puede teletransportarse a las rutas 6 y 8 (dos teletransportes); si se sale de la ruta 2, Abra puede 
llegar a las rutas 7 y 9 (dos teletransportes más); iniciando desde la ruta 3, se puede arribar a las rutas 4 y 8 (se suman nuevamente dos); 
si se arranca desde la ruta 4, las posibilidades son las rutas 3, 9 y 0 (ahora se acumulan tres teletransportes); pero si la posición inicial 
es la ruta 5, Abra no puede teletransportarse a ningún lugar dado que no hay teletransportes válidos.

Sin embargo, aún restan varias posibilidades más para seguir probando; desde la ruta 6 se pueden alcanzar las rutas 1, 7 y 0 (nuevamente se 
agregan tres más); por su parte desde la ruta 7 se puede mover a Abra hasta las rutas 2 y 6 (la cantidad se incrementa en dos); si se toma la 
ruta 8 como inicio, se pueden alcanzar las rutas 1 y 3 (se adicionan dos teletransportes); si se posiciona a Abra en la ruta 9, las opciones 
para teletransportarse son las rutas 2 y 4 (nuevamente se tienen dos teletransportes); y por último, si se sale desde la ruta 0, los 
teletransportes válidos son hacia las rutas 4 y 6 (se suman los últimos dos). En total, se pueden realizar veinte teletransportes válidos con 
Abra.

Ahora, diseña un algoritmo que permita calcular cuántos posibles teletransportes válidos puede realizar Abra, recibiendo como entrada la 
cantidad de teletransportes a realizar desde el inicio, partiendo de todas las rutas. Por ejemplo, como mostramos anteriormente, si la 
cantidad de teletransportes es uno, la cantidad de teletransportes válidos son veinte. Pero si la cantidad de teletransportes son dos y se 
sale de la ruta 1, se puede ir hasta las rutas 6 y 8 (un teletransporte), a continuación, a partir de la ruta 6 hasta las rutas 1, 7 y 0 
(dos teletransportes de Abra), luego se sigue desde la ruta 8 hasta las rutas 1 y 3 (para alcanzar los dos teletransportes de Abra). 
En resumen, se tienen cinco posibles teletransportes válidos partiendo desde la ruta 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben 
sumar todos los teletransportes que resulten de partir de las demás rutas. En total, la cantidad de posibles teletransportes válidos para dos 
teletransportes son 46. Una vez desarrollado el algoritmo, completa la siguiente tabla.
"""

# Implementamos las herramientas necesarias
class nodoArista(object):
    def __init__(self, info , destino):
        self.info = info
        self.destino = destino
        self.sig = None
class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()
class Grafo(object):
    def __init__(self, dirigido = True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamaño = 0
class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar_vertice(grafo, dato):
        nodo = nodoVertice(dato)
        if (grafo.inicio is None or grafo.inicio.info > dato):
            nodo.sig = grafo.inicio
            grafo.inicio = nodo
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while(act is not None and act.info < dato):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        grafo.tamaño += 1


red_pokemon = Grafo(False)
# Tenemos 8 vertices
ruta = input("Ingrese la ruta: ")
i = 0
while(i < 8):
    Arista.insertar_vertice(red_pokemon, ruta)
    ruta = input("Ingrese la ruta: ")
    i += 1
# El grafo generara un matriz de adyacencia de 8x8 la cual si la elevamos a lo que sea obtendremos el rsultado de los posibles teletransportes
def Matriz_Grafo(grafo):
    matriz = []
    aux = grafo.inicio
    while(aux is not None):
        aux2 = aux.adyacentes.inicio
        lista = []
        while(aux2 is not None):
            lista.append(aux2.destino.info)
            aux2 = aux2.sig
        matriz.append(lista)
        aux = aux.sig
    return matriz



# using LinearAlgebra

#La matriz Z es la matriz de adyacencia del grafo. 
#Para la construcción de la matriz Z lo que hemos hecho es tomar los vértices del grafo
#y ver como estaban conectadas esas posiciones según los movimientos que pued realizar la ficha del caballo.

# Ahora deberiamos hacer el resultado la funcion elevada...
Z = Matriz_Grafo(red_pokemon)
sum(Z^2)
sum(Z^3)
sum(Z^4)
sum(Z^5)
sum(Z^8)
sum(Z^10)
sum(Z^15)
sum(Z^18)
sum(Z^21)
sum(Z^23)
sum(Z^32)
