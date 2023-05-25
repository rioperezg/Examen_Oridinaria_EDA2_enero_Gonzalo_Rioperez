"""
Copia el ejercicio anterior y realicemos la siguiente modificación:

Junto al método init y clasificacion, sobrescriba el método especial de Python, el método str, que tiene el siguiente formato:

def __str__(self):
return "Lo que quiero mostrar"
Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto pokemon1 creado y realizamos 
print(pokemon1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea 
en un string).

2.2 Experimentación (0,5 puntos)
Implementa el método str y haz que muestre el nombre y el tipo del Pokemon. Crea una lista con un numero arbitrario de objetos tipo Pokemon. 
Recorre los elementos de la lista, y utiliza el método print de esos objetos para visualizar por pantalla la información del str.
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


i = random.randint(1, 7)
# random.sample(list_vehic, 3)
# Experimentacion
import unittest, random
lista_pokemon = []
class TestPokemon(unittest.TestCase):