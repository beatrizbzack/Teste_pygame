import pygame 

peach = pygame.image.load("C:/Users/bebec/OneDrive/Área de Trabalho/Super-Peach-Bros/Peachzinha.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(peach, (60,80))
        self.rect = self.image.get_rect(topleft = pos) 
        # Vector2 = lista que contem valores para x e y
        # vc pode colocar um vector para descrever a posição de um retangulo, sem ter q passar X e Y (vai direto)
        # e tbm pode acessar esses valores separadamente para cada index (nao perde eles)
        
        # player movement 
        self.direction = pygame.math.Vector2(0,0) 
        self.speed = 6 
        self.gravidade = 1 
        self.jump_speed = -12  

    
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            
        elif keys[pygame.K_LEFT]:
            self.direction.x = - 1 
        else: 
            self.direction.x = 0 

        if keys[pygame.K_SPACE]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravidade
        self.rect.y += self.direction.y 

    def jump(self):
        self.direction.y = self.jump_speed
 
            
    def update(self):
        self.get_input()
       
