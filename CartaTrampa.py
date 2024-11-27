from Carta import *
from Posicion import *
from Orientacion import *
from TipoAtributo import *
from TipoMonstruo import *

class CartaTrampa (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,atributo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__atributo = atributo

  def getAtributo (self):
      return self.__atributo
  
  def activar(self,cartaAtacante):
    if self.__atributo == cartaAtacante.getAtributo():
      print(f"Carta Trampa:\n{self.__nombre} , detiene el ataque de un monstruo con atributo {self.__atributo}")

  def __str__(self):
    return f"Carta Trampa: \n{self.getNombre()} , detiene el ataque de un monstruo con atributo {self.__atributo}"
