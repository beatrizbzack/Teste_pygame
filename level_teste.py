import pygame
from tiles import Tiles, Castelo, Estrela  
from settings import tile_size, jan_largura, jan_altura 
from player import Player  

class Level:
    def __init__(self, level_data, surface):
        # Level setup
        self.display_surface = surface 
        self.setup_level(level_data)
        self.world_shift = 0 # futuramente o player deve influenciar isso

    def setup_level(self, layout):
        # Cria grupo com todas as tiles do jogo, como sprites
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.decoracao = pygame.sprite.Group()
        self.estrela = pygame.sprite.Group() 

        for row_i, row in enumerate(layout): # passa por cada index da lista, tanto em  valor quanto em número
            for col_i, col in enumerate(row):
                if col == 'X': # Plotar tiles
                    # multiplicar pelo tamanho do tile = para dimensionar (escala dos indexes é pequena)
                    x = col_i * tile_size # esquerda e direita
                    y = row_i * tile_size # p/ cima e p/ baixo
                    tile = Tiles((x,y), tile_size)
                    self.tiles.add(tile)
                if col == 'P': # Plotar pos inicial do Player
                    x = col_i * tile_size
                    y = (row_i * tile_size) - 20 # Ajusta a posição da peach
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if col == 'C': # Plotar decoração do castelo
                    x = col_i * tile_size
                    y = row_i * tile_size
                    castle = Castelo((x,y))
                    self.decoracao.add(castle)
                if col_i == 'S': # Plotar estrela de fim de jogo
                    x = col_i * tile_size
                    y = row_i * tile_size
                    estrelinha = Estrela((x,y), tile_size) 
                    self.estrela.add(estrelinha)
                     


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx 
        direction_x = player.direction.x   

        if player_x < jan_largura/5 and direction_x < 0: # e se esta se mexendo para a esquerda
            self.world_shift = 6 
            player.speed = 0 
        elif player_x > (jan_largura - jan_largura/4) and direction_x > 0: # e se esta se mexendo para a direita
            self.world_shift = -6 
            player.speed = 0 
        else:
           self. world_shift = 0 
           player.speed = 6  

    def mov_col_horizontal(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed # velocidade ja estabelecida pelo re 

        for sprite in self.tiles.sprites(): # passa por todas as sprites de tiles
            if sprite.rect.colliderect(player.rect): # checa se tem alg colisão delas com o player (rect)
                if player.direction.x < 0: # left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0: # right
                    player.rect.right = sprite.rect.left 

    def mov_col_vertical(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites(): # passa por todas as sprites de tiles
            if sprite.rect.colliderect(player.rect): # checa se tem alg colisão delas com o player (rect)
                if player.direction.y > 0: # colisao de baixo
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0 # cancela a gravidade para quando ele ta no chao 
                elif player.direction.y < 0: # colisao de cima
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 


    def run(self):
        # Tiles
        self.decoracao.update(self.world_shift)
        self.tiles.update(self.world_shift) # visão do mapa (argumento de velocidade de mov)
        #self.estrela.update(self.world_shift)

        # Desenhar na tela 
        self.decoracao.draw(self.display_surface)
        self.tiles.draw(self.display_surface) # desenhar o mapa
        self.estrela.draw(self.display_surface) 

        self.scroll_x()
        
        # Player
        self.player.update()
        self.mov_col_horizontal()
        self.mov_col_vertical() 
        self.player.draw(self.display_surface)
        


