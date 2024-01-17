from cProfile import run
import pygame


class Hitbox():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.attack_type = 0
        self.attacking = False
        self.attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, 1 * self.rect.width, self.rect.height)
        self.attack_count = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0,0), self.rect,1)
        if self.attacking and self.attack_count > 0:
            pygame.draw.rect(surface, (0, 255, 0,0), self.attacking_rect,1)
            self.attack_count -= 1


    def move(self,surface):
        key = pygame.key.get_pressed()
        # attack
        self.attack(surface)
        if key[pygame.K_c] or key[pygame.K_KP4]:
            if key[pygame.K_c]:
                self.attack_type = 1
            if key[pygame.K_KP4]:
                self.attack_type = 1

    def attack(self, surface):
        self.attacking = True
        self.attack_count = 20
        print("attack")

# pygame.init()

# screen = pygame.display.set_mode((444, 444))
# pygame.display.set_caption("Stickfight")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == 1073741916:
#                 print("NUM4")