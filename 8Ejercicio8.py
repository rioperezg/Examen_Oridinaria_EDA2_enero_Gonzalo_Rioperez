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
class EdgeNode:
    """Node in adjacency list representing an edge."""
    def __init__(self, weight, destination):
        self.weight = weight
        self.destination = destination
        self.next = None

class EdgeList:
    """Adjacency list storing EdgeNode instances."""
    def __init__(self):
        self.head = None
        self.size = 0

class VertexNode:
    """Node representing a vertex in the graph."""
    def __init__(self, key):
        self.key = key
        self.next = None
        self.visited = False
        self.adjacents = EdgeList()

class Graph:
    """Graph implemented as an adjacency list. Directed by default."""
    def __init__(self, directed=True):
        self.head = None
        self.directed = directed
        self.size = 0

def insert_vertex(graph, key):
    """
    Insert a vertex with the given key into the graph in sorted order.
    Returns the new VertexNode.
    """
    node = VertexNode(key)
    if graph.head is None or graph.head.key > key:
        node.next = graph.head
        graph.head = node
    else:
        prev = graph.head
        curr = graph.head.next
        while curr and curr.key < key:
            prev = curr
            curr = curr.next
        node.next = curr
        prev.next = node
    graph.size += 1
    return node

def insert_edge(graph, weight, origin, destination):
    """
    Insert an edge of given weight from origin to destination.
    origin and destination are VertexNode instances.
    """
    add_edge(origin.adjacents, weight, destination.key)
    if not graph.directed:
        add_edge(destination.adjacents, weight, origin.key)

def add_edge(edge_list, weight, destination_key):
    """
    Add an edge to the adjacency list edge_list.
    """
    node = EdgeNode(weight, destination_key)
    if edge_list.head is None or edge_list.head.destination > destination_key:
        node.next = edge_list.head
        edge_list.head = node
    else:
        prev = edge_list.head
        curr = edge_list.head.next
        while curr and curr.destination < destination_key:
            prev = curr
            curr = curr.next
        node.next = curr
        prev.next = node
    edge_list.size += 1

def remove_vertex(graph, key):
    """
    Remove the vertex with the given key from the graph.
    Returns the removed key, or None if not found.
    """
    removed = None
    if graph.head and graph.head.key == key:
        removed = graph.head.key
        graph.head = graph.head.next
        graph.size -= 1
    else:
        prev = graph.head
        curr = graph.head.next if graph.head else None
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        if curr:
            removed = curr.key
            prev.next = curr.next
            graph.size -= 1
    if removed is not None:
        # remove all edges to this vertex
        v = graph.head
        while v:
            remove_edge(v.adjacents, key)
            v = v.next
    return removed

def graph_size(graph):
    """Return the number of vertices in the graph."""
    return graph.size

def is_graph_empty(graph):
    """Return True if the graph has no vertices."""
    return graph.head is None

def remove_edge(edge_list, destination_key):
    """
    Remove an edge to destination_key from edge_list.
    Returns the removed weight, or None if not found.
    """
    removed = None
    if edge_list.head and edge_list.head.destination == destination_key:
        removed = edge_list.head.weight
        edge_list.head = edge_list.head.next
        edge_list.size -= 1
    else:
        prev = edge_list.head
        curr = edge_list.head.next if edge_list.head else None
        while curr and curr.destination != destination_key:
            prev = curr
            curr = curr.next
        if curr:
            removed = curr.weight
            prev.next = curr.next
            edge_list.size -= 1
    return removed

def find_vertex(graph, key):
    """Return the VertexNode with the given key, or None if not found."""
    curr = graph.head
    while curr and curr.key != key:
        curr = curr.next
    return curr

def find_edge(vertex_node, destination_key):
    """Return the EdgeNode to destination_key, or None if not found."""
    curr = vertex_node.adjacents.head
    while curr and curr.destination != destination_key:
        curr = curr.next
    return curr

def path_exists(graph, origin, destination):
    """
    Return True if there's a path from origin to destination using DFS.
    origin and destination are VertexNode instances.
    """
    found = False
    if not origin.visited:
        origin.visited = True
        edge = origin.adjacents.head
        while edge and not found:
            v = find_vertex(graph, edge.destination)
            if v and v.key == destination.key:
                return True
            if v and not v.visited:
                found = path_exists(graph, v, destination)
            edge = edge.next
    return found

def reset_visited(graph):
    """Mark all vertices in the graph as not visited."""
    curr = graph.head
    while curr:
        curr.visited = False
        curr = curr.next

def traverse_vertices(graph):
    """Print all vertex keys in the graph."""
    curr = graph.head
    while curr:
        print(curr.key)
        curr = curr.next


def dfs(graph, vertex):
    """Depth-first traversal printing vertex keys."""
    curr = vertex
    while curr:
        if not curr.visited:
            curr.visited = True
            print(curr.key)
            edge = curr.adjacents.head
            while edge:
                v = find_vertex(graph, edge.destination)
                if v and not v.visited:
                    dfs(graph, v)
                edge = edge.next
        curr = curr.next

def bfs(graph, start_vertex):
    """Breadth-first traversal printing vertex keys using Cola."""
    queue = Cola()
    # Enqueue the starting vertex
    queue.arribo(start_vertex)
    start_vertex.visited = True
    while not queue.cola_vacia():
        node = queue.atencion()
        print(node.key)
        adj = node.adjacents.head
        while adj:
            v = find_vertex(graph, adj.destination)
            if v and not v.visited:
                v.visited = True
                queue.arribo(v)
            adj = adj.next

class nodoCola(object):
    info, sig = None, None
class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0
    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
            cola.tamaño -= 1
        return dato
    def cola_vacia(cola):
        return cola.frente is None
    def en_frente(cola):
        return cola.frente.info
    def tamaño(cola):
        return cola.tamaño
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arribo(cola,dato)
        return dato
    # Primera forma barrido, ineficiente(n^2)
    def barrido(cola):
        caux = Cola()
        while(not Cola.cola_vacia(cola)):
            dato = Cola.atencion(cola)
            print(dato)
            Cola.arribo(caux, dato)
        while(not Cola.cola_vacia(caux)):
            dato = Cola.atencion(caux)
            Cola.arribo(cola,dato)
    # Segunda forma barrido, eficiente(n)
    def barrido2(cola):
        i = 0
        while(i < Cola.tamaño(cola)):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1


def topological_sort(graph):
    in_deg = {v.key: 0 for v in traverse_vertices(graph)}
    # Calcular grados de entrada
    v = graph.head
    while v:
        e = v.adjacents.head
        while e:
            in_deg[e.destination] += 1
            e = e.next
        v = v.next
    # Cola para grado cero
    Q = []
    for key, deg in in_deg.items():
        if deg == 0: Q.append(key)
    topo = []
    while Q:
        u_key = Q.pop(0)
        topo.append(u_key)
        u = find_vertex(graph, u_key)
        e = u.adjacents.head
        while e:
            in_deg[e.destination] -= 1
            if in_deg[e.destination] == 0:
                Q.append(e.destination)
            e = e.next
    return topo


ES = {v.key: float('-inf') for v in traverse_vertices(graph)}
EF = {}
ES['S'] = 0



def forward_pass(graph, topo):
    ES = {v.key: float('-inf') for v in traverse_vertices(graph)}
    ES['S'] = 0
    for u_key in topo:
        u = find_vertex(graph, u_key)
        for e in iterate_edges(u):
            v_key = e.destination
            ES[v_key] = max(ES[v_key], ES[u_key] + e.weight)
    return ES

def backward_pass(graph, topo, ES):
    LF = {v.key: float('inf') for v in traverse_vertices(graph)}
    LF['T'] = ES['T']
    LS = {}
    for u_key in reversed(topo):
        LS[u_key] = LF[u_key]
        # Para cada arista p→u:
        for p, w in iterate_incoming_edges(graph, u_key):
            LF[p.key] = min(LF[p.key], LS[u_key] - w)
    return LS

# Uso:
topo = topological_sort(graph)
ES  = forward_pass(graph, topo)
LS  = backward_pass(graph, topo, ES)







