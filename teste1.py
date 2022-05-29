# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import sys
from settings import *
from tiles import * 
from level_teste import * 

pygame.init() # inicia framework

# ----- Gera tela principal

window = pygame.display.set_mode((jan_largura, jan_altura)) 
clock = pygame.time.Clock()
FPS = 60
level = Level(nivel_mapa, window) # acesso ao nível

# test_tile = pygame.sprite.Group(Tiles((100,100), 200))

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while True: # Enquanto game for verdade
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ----- Gera saídas 
    window.fill((0, 200, 253))  # Preenche com a cor branca
    #test_tile.draw(window)
    level.run()

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador
    clock.tick(FPS)
# ===== Finalização =====
# pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
# sys.exit()
