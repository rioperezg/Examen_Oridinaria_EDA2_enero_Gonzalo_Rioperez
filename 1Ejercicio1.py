"""
Crea una clase llamada Pokemon.py que tenga los atributos nombre y tipo. Crea el constructor de la clase. Añadir en el constructor un print 
para informar de que el Pokemon se ha creado con éxito. Crear un método llamado clasificacion que clasifique a los Pokemon según su tipo de 
la siguiente manera:

los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.

1.2 Experimentación (0,5 Puntos)

Crea una lista con un numero arbitrario de objetos tipo Pokemon. Recorre los elementos de la lista, y prueba a ejecutar el método 
clasificacion de cada objeto que has creado.
"""
# Empecemos por Agua
print("Bienvenido al programa de clasificacion de pokemon")
print("Introduzca las caracteristicas para tipo agua: ")
tipo_agua_ps = input("Introduzca los PS: ")
tipo_agua_ataque = input("Introduzca el ataque: ")
tipo_agua_ataque_esp = input("Introduzca el ataque especial: ")
tipo_agua_defensa_esp = input("Introduzca la defensa especial: ")
tipo_agua_velocidad = input("Introduzca la velocidad: ")

print("Bienvenido al programa de clasificacion de pokemon")
print("Introduzca las caracteristicas para tipo Fuego: ")
tipo_fuego_ps = input("Introduzca los PS: ")
tipo_fuego_ataque = input("Introduzca el ataque: ")
tipo_fuego_ataque_esp = input("Introduzca el ataque especial: ")
tipo_fuego_defensa_esp = input("Introduzca la defensa especial: ")
tipo_fuego_velocidad = input("Introduzca la velocidad: ")

print("Bienvenido al programa de clasificacion de pokemon")
print("Introduzca las caracteristicas para tipo Tierra: ")
tipo_tierra_ps = input("Introduzca los PS: ")
tipo_tierra_ataque = input("Introduzca el ataque: ")
tipo_tierra_ataque_esp = input("Introduzca el ataque especial: ")
tipo_tierra_defensa_esp = input("Introduzca la defensa especial: ")
tipo_tierra_velocidad = input("Introduzca la velocidad: ")

print("Bienvenido al programa de clasificacion de pokemon")
print("Introduzca las caracteristicas para tipo Tierra: ")
tipo_electrico_ps = input("Introduzca los PS: ")
tipo_electrico_ataque = input("Introduzca el ataque: ")
tipo_electrico_ataque_esp = input("Introduzca el ataque especial: ")
tipo_electrico_defensa_esp = input("Introduzca la defensa especial: ")
tipo_electrico_velocidad = input("Introduzca la velocidad: ")

print("Bienvenido al programa de clasificacion de pokemon")
print("Introduzca las caracteristicas para tipo Normal: ")
tipo_Normal_ps = input("Introduzca los PS: ")
tipo_Normal_ataque = input("Introduzca el ataque: ")
tipo_Normal_ataque_esp = input("Introduzca el ataque especial: ")
tipo_Normal_defensa_esp = input("Introduzca la defensa especial: ")
tipo_Normal_velocidad = input("Introduzca la velocidad: ")

print("Bienvenido al programa de clasificacion de pokemon")
print("Introduzca las caracteristicas para tipo Fantasma: ")
tipo_Fantasma_ps = input("Introduzca los PS: ")
tipo_Fantasma_ataque = input("Introduzca el ataque: ")
tipo_Fantasma_ataque_esp = input("Introduzca el ataque especial: ")
tipo_Fantasma_defensa_esp = input("Introduzca la defensa especial: ")
tipo_Fantasma_velocidad = input("Introduzca la velocidad: ")



class Pokemon(object):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("El pokemon se ha creado con exito")

    # Ahora pasaremos a crear un metodo clasificacion que clasifique a los pokemon segun su tipo de la la siguiente manera:
    # los PS, el Ataque, la Defensa, el Ataque Especial, la Defensa Especial y la Velocidad.
    def clasificacion(self, tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad):
        if tipo == "Agua":
            Ps = tipo_agua_ps
            Ataque = tipo_agua_ataque
            Ataque_Especial = tipo_agua_ataque_esp
            Defensa_Especial = tipo_agua_defensa_esp
            Velocidad = tipo_agua_velocidad
            return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad)
        elif tipo == "Electrico":
            Ps = tipo_electrico_ps
            Ataque = tipo_electrico_ataque
            Ataque_Especial = tipo_electrico_ataque_esp
            Defensa_Especial = tipo_electrico_defensa_esp
            Velocidad = tipo_electrico_velocidad
            return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad)
        elif tipo == "Fuego":
            Ps = tipo_fuego_ps
            Ataque = tipo_fuego_ataque
            Ataque_Especial = tipo_fuego_ataque_esp
            Defensa_Especial = tipo_fuego_defensa_esp
            Velocidad = tipo_fuego_velocidad
            return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad)
        elif tipo == "Tierra":
            Ps = tipo_tierra_ps
            Ataque = tipo_tierra_ataque
            Ataque_Especial = tipo_tierra_ataque_esp
            Defensa_Especial = tipo_tierra_defensa_esp
            Velocidad = tipo_tierra_velocidad
            return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad)
        elif tipo == "Fantasma":
            Ps = tipo_Fantasma_ps
            Ataque = tipo_Fantasma_ataque
            Ataque_Especial = tipo_Fantasma_ataque_esp
            Defensa_Especial = tipo_Fantasma_defensa_esp
            Velocidad = tipo_Fantasma_velocidad
            return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad)

        elif tipo == "Normal":
            Ps = tipo_Normal_ps
            Ataque = tipo_Normal_ataque
            Ataque_Especial = tipo_Normal_ataque_esp
            Defensa_Especial = tipo_Normal_defensa_esp
            Velocidad = tipo_Normal_velocidad
            return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, PS, Ataque, Defensa, Ataque_Especial, Defensa_Especial, Velocidad)



"""
        self.tipo_ps = tipo_ps
        self.tipo_ataque = tipo_ataque
        self.tipo_ataque_esp = tipo_ataque_esp  
        self.tipo_defensa_esp = tipo_defensa_esp
        self.tipo_velocidad = tipo_velocidad
        return "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(self.nombre, self.tipo, self.tipo_ps, self.tipo_ataque, self.tipo_ataque_esp, self.tipo_defensa_esp, self.tipo_velocidad)
"""

i = random.randint(1, 7)
# random.sample(list_vehic, 3)
# Experimentacion
import unittest, random
lista_pokemon = []
class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon1 = Pokemon("Pikachu", "Electrico")
        self.pokemon2 = Pokemon("Charmander", "Fuego")
        self.pokemon3 = Pokemon("Squirtle", "Agua")
        self.pokemon4 = Pokemon("Bulbasaur", "Planta")
        self.pokemon5 = Pokemon("Onix", "Tierra")
        self.pokemon6 = Pokemon("Gastly", "Fantasma")
        self.pokemon7 = Pokemon("Snorlax", "Normal")
        lista_pokemon.append(self.pokemon1)
        lista_pokemon.append(self.pokemon2)
        lista_pokemon.append(self.pokemon3)
        lista_pokemon.append(self.pokemon4)
        lista_pokemon.append(self.pokemon5)
        lista_pokemon.append(self.pokemon6)
        lista_pokemon.append(self.pokemon7)
    def test_clasificacion(self, lista_pokemon):
        lista_pokemon = random.sample(lista_pokemon, i)
        if lista_pokemon == []:
            print("No hay pokemon")
        else:
            pokemon = lista_pokemon[0]
            lista_pokemon.remove(pokemon)
            self.assertEqual(pokemon.clasificacion(pokemon.tipo, tipo_agua_ps, tipo_agua_ataque, tipo_agua_ataque_esp, tipo_agua_defensa_esp, tipo_agua_velocidad), "El pokemon {}, de tipo {} tiene {} PS, {} de ataque, {} de ataque especial, {} de defensa especial y {} de velocidad".format(pokemon.nombre, pokemon.tipo, tipo_agua_ps, tipo_agua_ataque, tipo_agua_ataque_esp, tipo_agua_defensa_esp, tipo_agua_velocidad))
            return TestPokemon.test_clasificacion(self, lista_pokemon)