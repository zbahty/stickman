from cProfile import run
import pygame


class hitbox():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.attack_type = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def attack(self):
        # attack
        self.attack(surface)
        if key[pygame.K_c] or key[pygame.K_KP4]:
            if key[pygame.K_c]:
                self.attack_type = 1
            if key[pygame.K_KP4]:
                self.attack_type = 1

    def attack(self, surface):
        attacking_rect = pygame.Rect(
            self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

# pygame.init()

# screen = pygame.display.set_mode((444, 444))
# pygame.display.set_caption("Stickfight")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == 1073741916:
#                 print("NUM4")
