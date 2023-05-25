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
    def clasificacion(self, tipo_ps, tipo_ataque, tipo_ataque_esp, tipo_defensa_esp, tipo_velocidad):
        self.tipo_ps = tipo_ps
        self.tipo_ataque = tipo_ataque
        self.tipo_ataque_esp = tipo_ataque_esp  
        self.tipo_defensa_esp = tipo_defensa_esp
        self.tipo_velocidad = tipo_velocidad
        return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, self.tipo_ps, self.tipo_ataque, self.tipo_ataque_esp, self.tipo_defensa_esp, self.tipo_velocidad)
       


# random.sample(list_vehic, 3)
# Experimentacion
import unittest, random
class TestPokemon(unittest.TestCase):
    lista_pokemon = []
    def setUp(self):
        lista_pokemon = []
        self.pokemon1 = Pokemon("Pikachu", "Electrico")
        self.pokemon2 = Pokemon("Charmander", "Fuego")
        self.pokemon3 = Pokemon("Squirtle", "Agua")
        self.pokemon4 = Pokemon("Bulbasaur", "Planta")
        self.pokemon5 = Pokemon("Onix", "Tierra")
        self.pokemon6 = Pokemon("Gastly", "Fantasma")
        self.pokemon7 = Pokemon("Snorlax", "Normal")
        lista_pokemon = [self.pokemon1, self.pokemon2, self.pokemon3, self.pokemon4, self.pokemon5, self.pokemon6, self.pokemon7]
    def test_clasificacion(self, lista_pokemon):
        

            # hAZTE CON TODOS poKEMON
       




        