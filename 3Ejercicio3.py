"""
Crea una clase llamada Pokeball.py que tenga los atributos peso, nombre, precio y fecha de fabricación. Crea el constructor de la clase. 
Añade en el constructor un print para informar de que la Pokeball se ha creado con éxito.

Crea el método str para visualizar por pantalla la información de las Pokeballs.

3.2 Experimentación (0,5 Puntos)
Crea algunas Pokeballs. Prueba a mostrar los datos de algunas Pokeballs ordenadas por su fecha de fabricación y a modificar algún valor, 
por ejemplo, prueba a modificar el precio de una de las Pokeballs
"""
class Pokeball(object):
    def __init__(self, peso, nombre, precio, fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        print("La pokeball se ha creado con exito")
    def __str__(self):
        return "La pokeball {} pesa {} gramos, cuesta {} euros y se fabrico el {}".format(self.nombre, self.peso, self.precio, self.fecha)
    
# Experimentacion
import unittest
class TestPokeball(unittest.TestCase):
    def setUp(self):
        self.pokeball1 = Pokeball(200, "Pokeball", 200, "20/04/2018")
        self.pokeball2 = Pokeball(300, "Superball", 600, "20/04/2018")
        self.pokeball3 = Pokeball(400, "Ultraball", 1200, "20/04/2018")
        self.pokeball4 = Pokeball(500, "Masterball", 3000, "20/04/2018")
    def test_str(self):
        self.assertEqual(str(self.pokeball1), "La pokeball Pokeball pesa 200 gramos, cuesta 200 euros y se fabrico el 20/04/2018")
        self.assertEqual(str(self.pokeball2), "La pokeball Superball pesa 300 gramos, cuesta 600 euros y se fabrico el 20/04/2018")
        self.assertEqual(str(self.pokeball3), "La pokeball Ultraball pesa 400 gramos, cuesta 1200 euros y se fabrico el 20/04/2018")
        self.assertEqual(str(self.pokeball4), "La pokeball Masterball pesa 500 gramos, cuesta 3000 euros y se fabrico el 20/04/2018")
