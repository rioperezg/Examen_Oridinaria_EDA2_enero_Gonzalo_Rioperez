"""
Crea una clase llamada Pokemon.py que tenga los atributos nombre y tipo. Crea el constructor de la clase. Añadir en el constructor un print 
para informar de que el Pokemon se ha creado con éxito. Crear un método llamado clasificacion que clasifique a los Pokemon según su tipo de 
la siguiente manera:

los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.

1.2 Experimentación (0,5 Puntos)

Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y prueba a ejecutar el método 
clasificacion de cada objeto que has creado.
"""
class Pokemon(object):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def __str__(self):
        return "El pokemon {}, de tipo {} se ha creado con exito".format(self.nombre, self.tipo)
    # Ahora pasaremos a crear un metodo clasificacion que clasifique a los pokemon segun su tipo de la la siguiente manera:
    # los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.
    def clasificacion(self):
        ps_Pokemon = int(input("Introduzca los Ps del Pokemon: "))
        Ataque = input("Introduzca el ataque del pokemon: ")
        Ataque_Esp = input("Introduzca el ataque especial del pokemon: ")
        Defensa_Esp = input("Introduzca la defensa especial del pokemon: ")
        Velocidad = input("Introduzca la velocidad del pokemon: ")
        


# Experimentacion
import unittest
class TestPokemon(unittest.TestCase):
    def setUp(self):

       




        