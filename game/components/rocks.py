import pygame
from game.utils.constants import ROCK_1, ROCK_2, ROCK_3, ROCK_4



class Rock:
    def __init__(self, image, x, y):
        self.image = image
        self.recta_x = x
        self.recta_y = y

    def get_x(self):#devuelve posicion 
        return self.recta_x

    def get_y(self):
        return self.recta_y

    def get_image(self):
        return self.image

    def set_y(self, y):#actualizar la posición en el eje y de la roca después de creacion
        self.recta_y = y
