"""
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-PokéBolas. 
Este problema consiste en ubicar n Pokémon en una red de gimnasios de tamaño n x n, sin que los mismos se enfrenten. Recuerda que un Pokémon 
puede moverse de manera horizontal, vertical y diagonal, además podemos ver una solución al problema de los 4 Pokémon. Nótese que una parte 
importante para resolver un problema es de qué manera representar la solución, para este caso particular usamos un vector de n posiciones 
(gimnasios) y el valor almacenado representa la fila donde se ubica dicho Pokémon.

 

Cuando hayas entendido el problema y tengas una solución en mente, desarrolla un algoritmo que permita hallar al menos una solución para 
distintas cantidades de Pokémon, y luego completa la siguiente tabla.
"""









# using LinearAlgebra

#La matriz Z es la matriz de adyacencia del grafo. 
#Para la construcción de la matriz Z lo que hemos hecho es tomar los vértices del grafo
#y ver como estaban conectadas esas posiciones según los movimientos que pued realizar la ficha del caballo.

Z= [0 0 0 0 0 1 0 1 0 0; 0 0 0 0 0 0 1 0 1 0; 0 0 0 1 0 0 0 1 0 0; 0 0 1 0 0 0 0 0 1 1; 0 0 0 0 0 0 0 0 0 0; 1 0 0 0 0 0 1 0 0 1; 0 1 0 0 0 1 0 0 0 0; 1 0 1 0 0 0 0 0 0 0; 0 1 0 1 0 0 0 0 0 0; 0 0 0 1 0 1 0 0 0 0]

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