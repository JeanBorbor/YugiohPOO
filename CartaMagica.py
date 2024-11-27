from Carta import *
from Posicion import *
from Orientacion import *
from TipoAtributo import *
from TipoMonstruo import *

class CartaMagica (Carta):
  def __init__(self, nombre, descripcion, posicion, orientacion,ataque, defensa,tipo):
    super().__init__(nombre, descripcion, posicion, orientacion)
    self.__tipo = tipo
    self.__defensa = defensa
    self.__ataque = ataque
  
  def getTipo (self):
    return self.__tipo
  def getAtaque (self):
    return self.__ataque
  def getDefena (self):
    return self.__defensa
    
  def usar (self,carta_monstruo):
    if self.__tipo == carta_monstruo.getTipo():
      if self.__defensa == 0:
        nuevo_ataque = carta_monstruo.getAtaque() + self.__ataque
        carta_monstruo.setAtaque(nuevo_ataque)
        print(self.__str__)
      if self.__ataque == 0:
        nueva_defensa = carta_monstruo.getDefensa() + self.__defensa
        carta_monstruo.setDefensa(nueva_defensa)
        print(self.__str__)
    else:
      print("No se puede usar, no son del mismo tipo Monstruo")
  
  def destruir (self,carta_monstruo):#NOT SURE
    if carta_monstruo.muere():
      return True

  def __str__(self):
    if self.__ataque == 0:
      return f"{self.getNombre()}, incrementa en {self.__defensa} la defensa de monstruos de tipo {self.__tipo}"
    else:
      return f"{self.getNombre()}, incrementa en {self.__ataque} la ataque de monstruos de tipo {self.__tipo}"