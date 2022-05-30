from numpy import tile
import pygame
from settings import *
from os import path 

# Imagens dos Tiles
chao = pygame.image.load("C:/Users/bebec/OneDrive/Área de Trabalho/DSoft/PYGAME/chao.png")
castelo = pygame.image.load("C:/Users/bebec/OneDrive/Área de Trabalho/DSoft/PYGAME/castelo.png")

# Chão
class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.transform.scale(chao, (size, size))
        self.rect = self.image.get_rect(topleft = pos)

    # atualizar a visão do mapa
    def update(self, x_shift):
        self.rect.x += x_shift 

# Castelo
class Castelo(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(castelo, (654,400))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift
     
