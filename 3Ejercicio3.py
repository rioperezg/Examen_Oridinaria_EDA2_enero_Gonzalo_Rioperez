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
    

