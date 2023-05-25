"""
Eres uno de los líderes de gimnasio (Gym Leader) de una importante organización Pokémon internacional. Uno de los altos miembros del 
Alto Mando te informa que el Campeón de la Liga Pokémon ha viajado desde EEUU a Barcelona y ha convocado un torneo de alto nivel para esta 
tarde a las 19:30 en Barcelona. Han consultado la lista de vuelos desde Madrid (donde estás tú) y han llegado a la conclusión de que tienes 
que tomar un vuelo que parte de Madrid dentro de 2 horas y cierra su facturación 20 minutos antes.

¿Qué duración mínima tiene la misión? ¿Llega el líder a facturar a tiempo dentro de los 100 minutos disponibles? Si no es así, revisa las 
dependencias, seguro que estás indicando relaciones basadas en las restricciones de los recursos.

Coloca primero la ruta crítica y sus recursos necesarios. A continuación, coloca y reajusta el resto de las actividades dentro de su holgura y 
define quién hará qué actividad.


Aquí tienes la tabla generada a partir de los datos proporcionados:

 

Ahora que tienes una lista de tareas y sus respectivas duraciones, necesitas decidir el camino más corto para completarlas todas. 
Considera cada tarea como un nodo y la duración como el peso de la arista que conecta las tareas. Algunas tareas deben completarse antes 
que otras, lo que implica que los nodos no están todos conectados entre sí.

Determinar la secuencia óptima de tareas. Recuerda que estos algoritmos son útiles para encontrar el árbol de expansión mínima en un grafo, 
lo que en este caso representaría la secuencia de tareas con el tiempo total mínimo.

¿Cuál algoritmo elegirías en este caso y por qué? Desarrolla y describe el proceso que utilizarías para aplicar este algoritmo al conjunto de 
tareas.
"""
# Consideramoscada como un nodo y luego haremos el arbol de expansion minima
class nodoArista(object):
    def __init__(self, info , destino):
        self.info = info
        self.destino = destino
        self.sig = None
class nodoVertice_Tareas(object):
    def __init__(self, info, Peso, descripcion):
        self.info = info
        self.Peso = Peso
        self.descripcion = descripcion
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
    def insertar_vertice(grafo, dato, Peso, descripcion):
        nodo = nodoVertice_Tareas(dato, Peso, descripcion)
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
    def agregar_arista(origen, dato, destino):
        nodo = nodoArista(dato, destino)
        if(origen.inicio is None or origen.inicio.destino > destino):
            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while(act is not None and act.destino < nodo.destino):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
            origen.tamaño += 1
    def insertar_arista(grafo, dato, origen, destino):
        Arista.agregar_arista(origen.adyacentes, dato, destino.info)
        if(not grafo.dirigido):
            Arista.agregar_arista(destino.adyacentes, dato, origen.info)
    def eliminar_vertice(grafo, clave):
        x = None 
        if(grafo.inicio.info == clave):
            x = grafo.inicio.info
            grafo.inicio = grafo.inicio.sig
            grafo.tamaño -= 1
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while(act is not None and act.info != clave):
                ant = act
                act = act.sig
            if(act is not None):
                x = act.info
                ant.sig = act.sig
                grafo.tamaño -= 1
        if(x is not None):
            aux = grafo.inicio
            while(aux is not None):
                if(aux.adyacentes.inicio is not None):
                    Arista.eliminar_arista(aux.adyacentes, clave)
                aux = aux.sig
        return x
    def barrido_vertices_con_eliminado(grafo, clave):
        aux = grafo.inicio
        if(aux is not None):
            Arista.eliminar_vertice(grafo, clave)




# Hemos de ver que nodos se conectan con otros que equivaldran a las aristas. Primero introducimos los nodos
nodo = input("(Pulse enter si quiere salir)Nodo: ")
peso = int(input("Peso: "))
Descripcion = input("Descripcion: ")
Peso = peso/100
Grafo_Tareas = Grafo()
while(nodo != "" or peso != 0 or Descripcion != ""):
    Arista.insertar_vertice(Grafo_Tareas, nodo, Peso, Descripcion)
    nodo = input("(Pulse enter si quiere salir)Nodo: ")
    peso = int(input("Peso: "))
    Descripcion = input("Descripcion: ")
    Peso = peso/100


# Ahora introducimos las aristas: Tenemos que ver que nodos se conectan con otros
# A no conecta con F; B no conecta con H; 
# Lo haremos de otro modo: Añadiremos un atributo descipcion a cada nodo y preguntaremos al usuario si se conecta con otro nodo






