from numpy import tile
import pygame
from settings import *
from os import path 

chao = pygame.image.load("C:/Users/bebec/OneDrive/Área de Trabalho/DSoft/PYGAME/chao.png")

class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(chao, (size, size))
        self.rect = self.image.get_rect(topleft = pos)

    # atualizar a visão do mapa
    def update(self, x_shift):
        self.rect.x += x_shift 